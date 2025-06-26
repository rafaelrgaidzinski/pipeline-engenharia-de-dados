# --------------------------
# Azure Data Lake Storage
# --------------------------
output "adls_name" {
  description = "Name of the created storage account"
  value       = azurerm_storage_account.storage.name
}

output "adls_dfs_endpoint" {
  description = "Primary DFS endpoint of the created storage account"
  value       = azurerm_storage_account.storage.primary_dfs_endpoint
}

output "adls_container_landing_zone" {
  description = "Name of the created storage container landing-zone"
  value       = azurerm_storage_container.landing-zone.name
}

output "adls_container_bronze" {
  description = "Name of the created storage container bronze"
  value       = azurerm_storage_container.bronze.name
}

output "adls_container_silver" {
  description = "Name of the created storage container silver"
  value       = azurerm_storage_container.silver.name
}

output "adls_container_gold" {
  description = "Name of the created storage container gold"
  value       = azurerm_storage_container.gold.name
}

# --------------------------
# Azure Databricks
# --------------------------
output "databricks_workspace_id" {
  description = "ID do Databricks Workspace"
  value       = azurerm_databricks_workspace.iac-databricks.id
}

output "databricks_workspace_url" {
  description = "URL do Databricks Workspace"
  value       = azurerm_databricks_workspace.iac-databricks.workspace_url
}

# --------------------------
# Azure SQL Server
# --------------------------
output "sqlserver_001" {
  description = "Nome do SQL Server"
  value       = azurerm_mssql_server.sql.name
}

output "database_001" {
  description = "Nome do Banco de Dados"
  value       = azurerm_mssql_database.sql.name
}

output "username" {
  description = "Usuário SQL Server"
  value       = var.usuario_admin
}

output "password" {
  description = "Senha SQL Server"
  value       = var.password
  sensitive   = true
}

# --------------------------
# IP público detectado
# --------------------------
output "public_ip" {
  description = "Meu IP Público"
  value       = data.ipify_ip.public.ip_cidr
}
