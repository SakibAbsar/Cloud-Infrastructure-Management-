
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "cloud-demo-rg"
  location = "West US"
}
