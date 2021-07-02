resource "random_resource1" "main" {}
resource "random_resource1" "name" {}
resource "random_resource2" "main" {}
resource "random_resource3" "main" {}

variable "in_main_file" {
  description = "Just antoher number."
  default     = "Value"
  type        = string
}
output "multiline4" {

  value       = one(server.main[*].id)
  description = "Description"

}