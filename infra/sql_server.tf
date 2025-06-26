resource "random_id" "name_unique" {
  byte_length = 8
}

resource "azurerm_mssql_server" "sql" {
  name                         = "sqlserver${random_id.name_unique.hex}"
  resource_group_name          = var.resource_group_name
  location                     = var.location
  version                      = "12.0"
  administrator_login          = var.usuario_admin
  administrator_login_password = var.password
}

resource "azurerm_mssql_database" "sql" {
  name                        = "ecommerce"
  server_id                   = azurerm_mssql_server.sql.id
  collation                   = "SQL_Latin1_General_CP1_CI_AS"
  sku_name                    = "Basic"
  max_size_gb                 = 2
  zone_redundant              = false
  storage_account_type        = "Local"
}

data "ipify_ip" "public" {}

resource "azurerm_mssql_firewall_rule" "sql" {
  name             = "RegraFWInternet"
  server_id        = azurerm_mssql_server.sql.id
  start_ip_address = data.ipify_ip.public.ip
  end_ip_address   = data.ipify_ip.public.ip
}
