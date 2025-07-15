import sys
import socket

logo = '''
   SSSSS   N   N   AAAAA   K   K   EEEEE
  S       NN  N   A   A   K  K    E
   SSSS  N N N   AAAAA   KKK     EEEE
      S  N  NN   A   A   K  K    E
  SSSSS  N   N   A   A   K   K   EEEEE
'''
print(logo)

# Known vulnerable service versions (example)
vulnerable_services = {
    'http': ['Apache/2.2.15', 'Microsoft-IIS/7.5'],
    'ftp': ['ProFTPD 1.3.3c', 'vsFTPd 2.3.4'],
    'ssh': ['OpenSSH 5.3', 'OpenSSH 7.2p2']
}

# Define a function for banner grabbing
def banner_grab(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return ''

# Check for command-line argument
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Argument, add hostname or IP")
    sys.exit()

print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            # Perform banner grabbing for certain ports
            banner = ''
            if port in [80, 443, 8080]:
                banner = banner_grab(target, port)
                print(f"Banner on port {port}: {banner}")
                # Check if banner indicates vulnerability
                for service, vuln_versions in vulnerable_services.items():
                    if service in banner:
                        for vuln_ver in vuln_versions:
                            if vuln_ver in banner:
                                print(f"[!] Vulnerable {service} version detected: {banner}")
            elif port == 22:
                banner = banner_grab(target, port)
                print(f"SSH Banner: {banner}")
                for vuln_ver in vulnerable_services['ssh']:
                    if vuln_ver in banner:
                        print(f"[!] Vulnerable SSH version detected: {banner}")
            elif port == 21:
                banner = banner_grab(target, port)
                print(f"FTP Banner: {banner}")
                for vuln_ver in vulnerable_services['ftp']:
                    if vuln_ver in banner:
                        print(f"[!] Vulnerable FTP version detected: {banner}")
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("\nHost name could not be resolved")
    sys.exit()
except socket.error:
    print("\nServer not responding")
    sys.exit()