provider "aws" {
  region = "us-east-1" # Specify your AWS region
}

resource "aws_instance" "example_server" {
  ami           ="ami-0a16e62504e6e52ce" # Replace with your selected AMI ID
  instance_type = "t2.micro"              # Choose your instance type
  key_name      = "devops"                # Replace with your SSH key name

  tags = {
    Name = "ExampleServer"
  }
}

output "server_ip" {
  value = aws_instance.example_server.public_ip
}


