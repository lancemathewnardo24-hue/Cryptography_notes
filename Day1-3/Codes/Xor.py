def fixed_xor(hex1, hex2):
   
    # decde hex int bytes
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
   
    # check lengths
    if len(b1) != len(b2):
        raise ValueError("Inputs must be the same length")
    
    # XOR each byte and return hex string
    return bytes(x ^ y for x, y in zip(b1, b2)).hex()

# Ask the user for two hex strings and print the XOR result
hex1 = input("Enter first hex string: ").strip()
hex2 = input("Enter second hex string: ").strip()
print("XOR result:", fixed_xor(hex1, hex2))