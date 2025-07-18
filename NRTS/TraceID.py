import socket
import os
import struct
import time
import platform

logo = '''
  TTTTT  RRRR   AAAAA  CCCCC  EEEEE  I   DDDD  
    T    R   R  A   A  C      E      I   D   D 
    T    RRRR   AAAAA  C      EEEE   I   D   D 
    T    R  R   A   A  C      E      I   D   D 
    T    R   R  A   A  CCCCC  EEEEE  I   DDDD  

'''

print(logo)

def create_packet():
    # Create a dummy packet
    return b'\x00' * 64  # 64 bytes of dummy data

def traceroute(destination, max_hops=30):
    # Create a raw socket
    icmp = socket.getprotobyname('icmp')
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    print(f"Traceroute to {destination} with a maximum of {max_hops} hops:")

    for ttl in range(1, max_hops + 1):
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
        sock.settimeout(2)  # Set a timeout for the response

        # Create a packet
        packet = create_packet()
        start_time = time.time()

        try:
            # Send the packet
            sock.sendto(packet, (destination, 33434))
            # Receive the response
            recv_packet, addr = sock.recvfrom(1024)
            round_trip_time = (time.time() - start_time) * 1000  # Convert to milliseconds

            print(f"{ttl:2d}  {addr[0]:<15}  {round_trip_time:.2f} ms")
        except socket.timeout:
            print(f"{ttl:2d}  * * * Request timed out.")
        except Exception as e:
            print(f"{ttl:2d}  Error: {e}")

    sock.close()

if __name__ == "__main__":
    destination_input = input("Enter the destination (e.g., google.com): ")
    traceroute(destination_input)
