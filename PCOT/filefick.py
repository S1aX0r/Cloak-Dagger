import hashlib
import os

logo = '''
FFFFF  IIIII  L      EEEEE  FFFFF  IIIII  CCCCC  K   K
F        I    L      E      F        I    C      K  K
FFFFF    I    L      EEEE   FFFF     I    C      KKK
F        I    L      E      F        I    C      K  K
F      IIIII  LLLLL  EEEEE  F      IIIII  CCCCC  K   K

F#CK up your targets files!
'''

print(logo)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()

def create_protected_file_from_existing(existing_file_path, new_file_path, password):
    if not os.path.exists(existing_file_path):
        return "The specified file does not exist."

    with open(existing_file_path, 'r') as f:
        content = f.read()

    hashed_password = hash_password(password)
    hashed_content = hash_content(content)
    
    with open(new_file_path, 'w') as f:
        f.write(hashed_password + '\n') 
        f.write(hashed_content)  

    return f"Password-protected file '{new_file_path}' created."

def read_protected_file(file_path, password):
    if not os.path.exists(file_path):
        return "File does not exist."

    with open(file_path, 'r') as f:
        stored_hashed_password = f.readline().strip()  
        hashed_content = f.read() 

    if hash_password(password) == stored_hashed_password:
        return f"Hashed content: {hashed_content}"
    else:
        return "Invalid password!"

if __name__ == "__main__":
    existing_file_path = input("Enter the path of the existing file to protect: ")
    new_file_path = input("Enter the path for the new password-protected file: ")
    password = input("Set a password for the new file: ")

    result = create_protected_file_from_existing(existing_file_path, new_file_path, password)
    print(result)

    read_password = input("Enter the password to read the new file: ")
    print(read_protected_file(new_file_path, read_password))
