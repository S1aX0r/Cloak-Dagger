import os

logo = r'''

  __                         _     
 / _|___  ___  __ _ _ __ ___| |__  
| |_/ __|/ _ \/ _` | '__/ __| '_ \ 
|  _\__ \  __/ (_| | | | (__| | | |
|_| |___/\___|\__,_|_|  \___|_| |_|

'''
print(logo)

def list_files_and_directories(path):
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            size = os.path.getsize(full_path)
            permissions = oct(os.stat(full_path).st_mode)[-3:]  # Get permissions in octal
            print(f"{permissions} | {size} bytes | {full_path}")

if __name__ == "__main__":
    path_to_scan = input("Insert path to scan: ")
    print(f"Listing files and directories in: {path_to_scan}")
    list_files_and_directories(path_to_scan)
