terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.9.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.0.0"
    }
    ipify = {
      source  = "rerichardjr/ipify"
      version = "1.0.0"
    }
  }
}

# Azure Provider
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

# Databricks Provider
provider "databricks" {
  azure_workspace_resource_id = azurerm_databricks_workspace.iac-databricks.id
  azure_client_id             = var.azure_client_id
  azure_client_secret         = var.azure_client_secret
  azure_tenant_id             = var.azure_tenant_id
}

# IPify Provider
provider "ipify" {
  # sem parâmetros obrigatórios
}
