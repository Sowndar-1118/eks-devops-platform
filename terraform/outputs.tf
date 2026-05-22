output "container_name" {
  value = docker_container.python_container.name
}

output "image_name" {
  value = docker_image.python_app.name
}
