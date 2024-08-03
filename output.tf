output "public_ip_addresses" {
  description = "Public IP addresses"
  value       = data.external.ip.result.public_ips
}

output "private_ip_addresses" {
  description = "Private IP addresses"
  value       = data.external.ip.result.private_ips
}
