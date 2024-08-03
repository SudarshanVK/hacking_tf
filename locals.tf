data "external" "ip" {
  program = ["python", "ip.py"]
  query = {
    ip_addresses = jsonencode(var.ip_addresses)
  }
}
