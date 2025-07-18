import requests

logo = '''
  W   W  EEEEE  B   B  FFFFF  I   N   N  DDDD  
  W   W  E      B   B  F      I   NN  N  D   D 
  W W W  EEEE   BBBBB  FFFF   I   N N N  D   D 
  W W W  E      B   B  F      I   N  NN  D   D 
   W W   EEEEE  B   B  F      I   N   N  DDDD  
'''
print(logo)

def http_content_scanner(url, wordlist):
    found_paths = []

    for path in wordlist:
        url = f"{url}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[*] Found: {url}")
            elif response.status_code == 404:
                print(f"[X] Not Found: {url}")
            elif response.status_code == 403:
                print(f"[!] Forbidden: {url}")
            else:
                print(f"[?] Status {response.status_code}: {url}")
        except requests.exceptions.RequestException as e:
                print(f"[X] Error accessing {url}: {e}")
    
    return found_paths

if __name__ == "__main__":
    target_url = input("Enter target URL: ").strip("/")
         
    wordlist = [
    "admin", "login", "uploads", "config.php", "backup", "robots.txt",
    "index.php", "test.php", "api", "images", "css", "js", "favicon.ico"
    ]

    print(f"Running WebFind on {target_url}")
    found = http_content_scanner(target_url, wordlist)

    if found:
        print(f"\nFound Paths: ")

        for path in found:
            print(path)

    else:
        print(f"\nNo Paths Found for: {target_url}")