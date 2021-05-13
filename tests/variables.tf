variable "empty" {}

variable "number" {

    description = "Just antoher number."

    type = number
    default = 100

    sensetive = true

}

variable "string-test-default" {

    description = "Just another description."
    
    type = string
    default = "string-test-value"

    sensitive = false
    
}

variable "string-test-type" {

    type = string

}