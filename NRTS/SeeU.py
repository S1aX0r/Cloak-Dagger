import socket

logo = '''
  SSSSS  EEEEE  EEEEE   U   U
  S      E      E       U   U
   SSSS  EEEE   EEEE    U   U
      S  E      E       U   U
  SSSSS  EEEEE  EEEEE    UUUU
'''
print(logo)


def create_socket(port):
    try:
        listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listener.bind(("0.0.0.0", port))  
        return listener
    except Exception as e:
        print(f"Error creating socket on port {port}: {e}")
        return None

def listen_for_packets(listeners):
    print("Listening for UDP packets on specified ports...")
    while True:
        try:
            for listener in listeners:
                data, addr = listener.recvfrom(1024)  # Buffer size
                print(f"Received packet from {addr} on port {listener.getsockname()[1]}: {data}")

        except KeyboardInterrupt:
            print("Listener stopped.")
            break
        except Exception as e:
            print(f"Error processing packet: {e}")

if __name__ == "__main__":
    ports_input = input("Enter the port(s) to listen on (comma-separated): ")
    ports = [int(port.strip()) for port in ports_input.split(",")]

    listeners = []
    for port in ports:
        listener = create_socket(port)
        if listener:
            listeners.append(listener)

    if listeners:
        listen_for_packets(listeners)
    else:
        print("No valid sockets created. Exiting.")
