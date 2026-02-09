# Crypto Challenge Set 1

## CryptoPals Rule (Important)
> Always operate on raw bytes, never on encoded strings.  
> Only use hex and base64 for pretty-printing.

### Meaning
- Hex and Base64 are only representations
- Cryptographic operations must be performed on raw byte data
- Incorrect handling of encodings can cause bugs and security issues

---
## **1st Challenge: Convert hex to base64**

### Task
Convert the following hex string into Base64:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

### Expected Output
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

### Conversion Python Code
[Open Base 64 Conversion crypto Program](Day1-3/Codes/01_HexToBase64.py)

## **2nd Challenge: Convert hex to base64**

Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

should produce:
746865206b696420646f6e277420706c6179

### XOR Code
[Open Function XOR](Day1-3/Codes/02_Xor.py)

## **3rd Challenge: Single Byte XOR cipher**

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

### Single Byte Decryptor Code
[Open SingleByteDecryptor](Day1-3/Codes/03_SingleByteDecryptXor.py)

## **4th Challenge: Detect single-character XOR**

One of the 60-character strings in [this file](Day1-3/Codes/Data.txt) has been encrypted by single-character XOR.

Find it.

>Your code from [#3](Day1-3/Codes/03_SingleByteDecryptXor.py) should help.

### File Decryptor XOR Code
[Open FIle FileDecryptorXOR](Day1-3/Codes/04_FileXorDecrypt.py)


