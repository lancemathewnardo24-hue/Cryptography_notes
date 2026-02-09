import os

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
    return sum(ENGLISH_FREQ.get(c, 0) for c in text.lower())

def single_byte_xor(data, key):
    return bytes(b ^ key for b in data)

# Track best result
best_score = 0
best_result = None
best_key = None
best_line = None

# Get directory where THIS script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ask for filename (Data.txt)
filename = input("Enter filename: ").strip()

# If user forgets .txt, add it
if not filename.endswith(".txt"):
    filename += ".txt"

# Build full path
file_path = os.path.join(BASE_DIR, filename)

# Debug info (you can remove later)
print("Opening:", file_path)

# Open file safely
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()

        try:
            cipher_bytes = bytes.fromhex(line)
        except ValueError:
            continue

        for key in range(256):
            decrypted = single_byte_xor(cipher_bytes, key)

            try:
                text = decrypted.decode("ascii")
            except UnicodeDecodeError:
                continue

            score = score_english(text)

            if score > best_score:
                best_score = score
                best_result = text
                best_key = key
                best_line = line

# Output result
print("\nSingle-byte XOR found")
print("Encrypted hex:", best_line)
print("Key:", chr(best_key), f"(decimal {best_key})")
print("Decrypted message:")
print(best_result)
