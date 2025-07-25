import socket

def fetch_http_headers(url):
    host = url.split("//")[-1].split("/")[0]
    port = 80
    request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())
        response = s.recv(4096)
        print(response.decode())

# Example usage
user_site = input("Insert site to get headers: ")
fetch_http_headers(user_site)
