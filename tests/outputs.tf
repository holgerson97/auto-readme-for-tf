output "oneline1" { value = one(server.main[*].id) }

output "multiline1" {

  value = one(server.main[*].id)

}
output "multiline2" {

  value       = one(server.main[*].id)
  description = "Description"

}
output "multiline3" {

  value       = one(server.main[*].id)
  description = "Description"
  sensitive   = true

}