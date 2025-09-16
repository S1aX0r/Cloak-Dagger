import os
import subprocess

logo = r'''
                                             _     
 _   _ ___  ___ _ __ ___  ___  __ _ _ __ ___| |__  
| | | / __|/ _ \ '__/ __|/ _ \/ _` | '__/ __| '_ \ 
| |_| \__ \  __/ |  \__ \  __/ (_| | | | (__| | | |
 \__,_|___/\___|_|  |___/\___|\__,_|_|  \___|_| |_|

'''
print(logo)

def get_user_accounts():
    if os.name == 'nt':  # Windows
        users = subprocess.check_output(['net', 'user']).decode().splitlines()[4:-1]
        return [user.split()[0] for user in users]
    else:  # Linux
        users = subprocess.check_output(['cut', '-d:', '-f1', '/etc/passwd']).decode().splitlines()
        return users

def get_last_login():
    if os.name == 'nt':  # Windows
        last_login = subprocess.check_output(['net', 'user']).decode()
        return last_login
    else:  # Linux
        last_login = subprocess.check_output(['last']).decode()
        return last_login

if __name__ == "__main__":
    print("User Accounts:")
    accounts = get_user_accounts()
    for account in accounts:
        print(account)
    print("\nLast Login Information:")
    print(get_last_login())
