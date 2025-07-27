import socket
import psutil

logo = '''
 N   N  EEEEE  TTTTT IIIII N   N  FFFFF  OOO  
 NN  N  E        T     I   NN  N  F     O   O 
 N N N  EEEE     T     I   N N N  FFFF  O   O 
 N  NN  E         T     I   N  NN  F     O   O 
 N   N  EEEEE     T   IIIII N   N  F      OOO  
'''
print(logo)


def network_interface_info():
    interfaces = psutil.net_if_addrs()
    for interface, addresses in interfaces.items():
        print(f"\nInterface: {interface}")
        for address in addresses:
            print(f"  Address: {address.address} (Family: {address.family})")

network_interface_info()
