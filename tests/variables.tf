variable "empty" {}
variable "oneline1" { description = "Description" }

variable "multiline1" {

  description = "Just antoher number."

}
variable "multiline2" {

  description = "Just antoher number."
  default     = "Value"

}
variable "multiline3" {

  description = "Just antoher number."
  default     = "Value"
  type        = string

}
variable "multiline4" {

  description = "Just antoher number."
  default     = "Value"
  type        = string
  sensitive   = true

}
variable "object" {

  description = "Just an object."
  default = {
    key   = "integer"
    value = 1
  }
  type = object({
    key   = string
    value = number
  })
  sensitive = true

}