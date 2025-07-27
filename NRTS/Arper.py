import os
import platform

logo = '''
  AAAAA  RRRR   PPPP   EEEEE  RRRR  
 A     A R   R  P   P  E      R   R 
 AAAAAAA RRRR   PPPP   EEEE   RRRR  
 A     A R  R   P      E      R  R  
 A     A R   R  P      EEEEE  R   R 
'''
print(logo)


def arp_scan():
    if platform.system() == "Windows":
        command = "arp -a"
    else:
        command = "arp -n"
    
    os.system(command)

arp_scan()
