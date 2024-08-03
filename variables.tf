variable "ip_addresses" {
  description = "List of private and public IP addresses"
  type        = list(string)
  default = [
    "192.168.1.10",   # Private IP address
    "10.0.0.25",      # Private IP address
    "172.16.5.100",   # Private IP address
    "192.168.100.50", # Private IP address
    "8.8.8.8",        # Public IP address (Google DNS)
    "8.8.4.4",        # Public IP address (Google DNS)
    "1.1.1.1",        # Public IP address (Cloudflare DNS)
    "9.9.9.9",        # Public IP address (Quad9 DNS)
    "198.51.100.1",   # Public IP address (Example)
    "93.184.216.34",  # Public IP address (Example)
  ]
}
