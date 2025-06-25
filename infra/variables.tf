# --------------------------
# Azure Data Lake Storage
# --------------------------
variable "resource_group_name" {
  description = "Nome do Resource Group do Databricks"
  type        = string
}

variable "location" {
  description = "Localização do Databricks"
  type        = string
  default     = "westus"
}

variable "subscription_id" {
  description = "ID da Subscription na Azure"
  type        = string
}

# --------------------------
# Azure Databricks
# --------------------------
variable "workspace_name" {
  description = "Nome do Workspace do Databricks"
  type        = string
}

variable "azure_client_id" {
  description = "Client ID da conta de serviço Azure (appID)"
  type        = string
}

variable "azure_client_secret" {
  description = "Client Secret da conta de serviço Azure (password)"
  type        = string
  sensitive   = true
}

variable "azure_tenant_id" {
  description = "Tenant ID da conta de serviço Azure (tenant)"
  type        = string
}

# --------------------------
# Azure SQL Server
# --------------------------
variable "usuario_admin" {
  description = "Usuário Admin do SQL Server"
  type        = string
}

variable "password" {
  description = "Senha do SQL Server"
  type        = string
  sensitive   = true
}