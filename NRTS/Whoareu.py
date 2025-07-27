import socket

logo = '''
W   W H   H  OOO   AAA  RRRR  EEEEE U   U
W   W H   H O   O A   A R   R E     U   U
W W W HHHHH O   O AAAAA RRRR  EEEE  U   U
WW WW H   H O   O A   A R R   E     U   U
W   W H   H  OOO  A   A R  RR EEEEE  UUU 
'''
print(logo)

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
