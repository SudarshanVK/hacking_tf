import json
import ipaddress
import sys
import logging

logging.basicConfig(
    filename="ip_classification.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def main():
    # Read the JSON input from Terraform
    input_data = json.load(sys.stdin)

    ip_addresses = json.loads(input_data["ip_addresses"])

    # Initialize empty lists to store private and public IP addresses
    private_ips = []
    public_ips = []

    # Loop through the list of IP addresses
    for ip in ip_addresses:
        # Convert the IP address to an ipaddress object
        ip_address = ipaddress.ip_address(ip)

        # Check if the IP address is public or private
        if ip_address.is_private:
            logging.info(f"{ip_address} is a Private IP address")
            private_ips.append(str(ip_address))
        else:
            logging.info(f"{ip_address} is a Public IP address")
            public_ips.append(str(ip_address))

    result = {
        "private_ips": json.dumps(private_ips),
        "public_ips": json.dumps(public_ips),
    }

    # Return the result back to Terraform
    json.dump(result, sys.stdout)


# Execute the main function to process the IP addresses
if __name__ == "__main__":
    main()
