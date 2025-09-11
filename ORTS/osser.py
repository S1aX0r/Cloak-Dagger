import socket
import platform

logo = r'''

  ___  ___ ___  ___ _ __ 
 / _ \/ __/ __|/ _ \ '__|
| (_) \__ \__ \  __/ |   
 \___/|___/___/\___|_|   

'''
print(logo)

def system_info():
    os_name = platform.system()
    os_version = platform.version()
    architecture = platform.architecture()[0]
    hostname = socket.gethostname()

    print(f"Operating System: {os_name} {os_version}")
    print(f"Architecture: {architecture}")
    print(f"Hostname: {hostname}")

if __name__ == "__main__":
    system_info()
