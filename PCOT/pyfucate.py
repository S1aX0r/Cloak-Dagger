logo = r'''
              __                 _       
 _ __  _   _ / _|_   _  ___ __ _| |_ ___ 
| '_ \| | | | |_| | | |/ __/ _` | __/ _ \
| |_) | |_| |  _| |_| | (_| (_| | ||  __/
| .__/ \__, |_|  \__,_|\___\__,_|\__\___|
|_|    |___/        

'''
print(logo)

def obfuscate_string(input_string, shift):
    obfuscated = ''.join(chr((ord(char) + shift) % 256) for char in input_string)
    return obfuscated

def deobfuscate_string(obfuscated_string, shift):
    deobfuscated = ''.join(chr((ord(char) - shift) % 256) for char in obfuscated_string)
    return deobfuscated

original_payload = input("Enter payload here --> ")
shift_value = 3
obfuscated_payload = obfuscate_string(original_payload, shift_value)
print(f'Obfuscated: {obfuscated_payload}')
response = input("Do you want to deobfuscate payload? y/n: ")

if response.lower() == "y":
    deobfuscated_payload = deobfuscate_string(obfuscated_payload, shift_value)
    print(f'Deobfuscated: {deobfuscated_payload}')

else:
    exit(1)
