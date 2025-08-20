import base64
import sys

logo = '''
PPPP    A   Y   Y CCCCC  OOO  DDDD  EEEEE
P   P  A A   Y Y  C     O   O D   D E    
PPPP  AAAAA   Y   C     O   O D   D EEEE 
P     A   A   Y   C     O   O D   D E    
P     A   A   Y   CCCCC  OOO  DDDD  EEEEE
'''
print(logo)

def encode_base64(payload):
    return base64.b64encode(payload.encode()).decode()

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 paycoder.py <payload> <encoding_format>")
        print("Encoding formats: base64")
        sys.exit(1)

    payload = sys.argv[1]
    encoding_format = sys.argv[2].lower()

    if encoding_format == 'base64':
        encoded_payload = encode_base64(payload)
    else:
        print("Invalid encoding format. Please choose 'base64'.")
        sys.exit(1)

    print(f"Encoded Payload ({encoding_format}): {encoded_payload}")

if __name__ == "__main__":
    main()
