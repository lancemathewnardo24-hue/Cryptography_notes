def xor_decrypt(hex_message, hex_key):
    message_bytes = bytes.fromhex(hex_message)
    key_byte = int(hex_key, 16)

    decrypted_bytes = bytes(b ^ key_byte for b in message_bytes)

    try:
        return decrypted_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return decrypted_bytes  # return raw bytes if not valid text

# ---- User Input ----
hex_message = input("Enter hex-encoded message: ")
hex_key = input("Enter 1-byte hex key (e.g. 1f): ")

result = xor_decrypt(hex_message, hex_key)

print("\nDecrypted output:")
print(result)