resource "docker_image" "python_app" {
  name = var.image_name

  build {
    context = "../app"
  }
}

resource "docker_container" "python_container" {
  image = docker_image.python_app.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = 5001
  }
}
