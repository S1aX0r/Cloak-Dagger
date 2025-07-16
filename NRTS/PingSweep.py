import os
import platform
import subprocess
import ipaddress

logo = '''
  PPPP   III  N   N  GGGG      SSSS  W   W  EEEEE  EEEEE  PPPP
  P   P   I   NN  N G         S      W   W  E      E      P   P
  PPPP    I   N N N G  GG     SSSS   W W W  EEEE   EEEE   PPPP
  P       I   N  NN G   G          S W W W  E      E      P
  P      III  N   N  GGGG      SSSS  W   W  EEEEE  EEEEE  P
'''

print(logo)

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', str(host)]
    
    return subprocess.call(command) == 0

def ping_sweep(subnet):
    try:
        network = ipaddress.ip_network(subnet)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    print(f"Pinging hosts in the subnet: {subnet}")
    
    for ip in network.hosts():
        ip_str = str(ip)
        print(f"Pinging {ip_str}...")
        if ping(ip_str):
            print(f"{ip_str} is alive")
        else:
            print(f"{ip_str} is not reachable")

if __name__ == "__main__":
    subnet_input = input("Enter the subnet (e.g., 192.168.1.0/24): ")
    print("Starting PingSweep...")
    ping_sweep(subnet_input)