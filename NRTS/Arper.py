import os
import platform

def arp_scan():
    if platform.system() == "Windows":
        command = "arp -a"
    else:
        command = "arp -n"
    
    os.system(command)

arp_scan()
