import base64

# Ask the user for hex input
hex_string = input("Enter hex string: ")

# Convert hex to raw bytes
try:
    raw_bytes = bytes.fromhex(hex_string)
except ValueError:
    print("Invalid hex input!")
    exit()

# Convert raw bytes to Base64
base64_bytes = base64.b64encode(raw_bytes)

# Convert bytes to string for printing
base64_string = base64_bytes.decode()

print("Base64 output:", base64_string)
