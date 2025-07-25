import socket

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address of {domain}: {ip_address}")
        
        mx_records = socket.getaddrinfo(domain, None)
        print(f"MX Records for {domain}: {mx_records}")
        
    except socket.gaierror:
        print(f"Could not resolve {domain}")

user_lookup = input("Enter domain / IP to look up: ")
dns_lookup(user_lookup)
