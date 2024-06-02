def validate(ip_address):
    # Split the IP address into its components
    parts = ip_address.split('.')
    
    # Check if the IP address has exactly four components
    if len(parts) != 4:
        return False
    
    # Check if each component is a valid integer in the range [0, 255]
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True

def main():
    ip_address = input("Enter an IPv4 address: ")
    if validate(ip_address):
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")

if __name__ == "__main__":
    main()
