#
# Creates a resource group for Book Catagory and Inventory Management Microservices.
#
resource "azurerm_resource_group" "sit722part5" {
  name     = var.app_name
  location = var.location
}