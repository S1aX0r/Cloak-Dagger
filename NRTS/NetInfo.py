import socket
import psutil

def network_interface_info():
    interfaces = psutil.net_if_addrs()
    for interface, addresses in interfaces.items():
        print(f"\nInterface: {interface}")
        for address in addresses:
            print(f"  Address: {address.address} (Family: {address.family})")

network_interface_info()
