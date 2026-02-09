# English character frequency (rough)
ENGLISH_FREQ = {
    'a': 0.065, 'b': 0.012, 'c': 0.022, 'd': 0.032,
    'e': 0.102, 'f': 0.021, 'g': 0.016, 'h': 0.049,
    'i': 0.057, 'j': 0.001, 'k': 0.005, 'l': 0.033,
    'm': 0.020, 'n': 0.057, 'o': 0.061, 'p': 0.015,
    'q': 0.001, 'r': 0.049, 's': 0.053, 't': 0.075,
    'u': 0.022, 'v': 0.008, 'w': 0.017, 'x': 0.001,
    'y': 0.014, 'z': 0.001, ' ': 0.13
}

def score_english(text):
    score = 0
    for char in text.lower():
        score += ENGLISH_FREQ.get(char, 0)
    return score

def single_byte_xor(cipher_bytes, key):
    return bytes(b ^ key for b in cipher_bytes)

hex_string = input("Enter hex string: ").strip()
cipher_bytes = bytes.fromhex(hex_string)

best_score = 0
best_result = None
best_key = None

for key in range(256):
    decrypted = single_byte_xor(cipher_bytes, key)
    try:
        decrypted_text = decrypted.decode('ascii')
    except UnicodeDecodeError:
        continue

    score = score_english(decrypted_text)

    if score > best_score:
        best_score = score
        best_result = decrypted_text
        best_key = key

print("\nBest result found:")
print("Key (ASCII):", chr(best_key))
print("Key (decimal):", best_key)
print("Decrypted message:")
print(best_result)