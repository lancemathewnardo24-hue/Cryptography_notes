# Day 1 – Encoding Basics (Hex & Base64)

## Overview
Day 1 focuses on understanding **encoding**, which is a foundational concept in cryptography.
Encoding changes how data is represented so it can be stored or transmitted safely, but it does
**not** provide security.

This knowledge is required before learning encryption techniques such as XOR and AES,
especially in CryptoPals Set 1.

---

## Learning Objectives
By the end of Day 1, I should be able to:
- Explain what encoding is
- Differentiate encoding from encryption and hashing
- Identify Hex and Base64 encoded data
- Convert Hex to raw bytes
- Encode raw bytes into Base64
- Explain why cryptographic operations work on bytes

---

## What is Encoding?
Encoding is the process of converting data from one format to another for compatibility
and readability.

**Important:** Encoding is reversible and provides **no security**.

Examples of encoding:
- Hexadecimal (Hex)
- Base64
- ASCII

---

## Hexadecimal (Hex)
Hexadecimal is a base-16 encoding system used to represent binary data.

### Key Characteristics
- Uses characters `0–9` and `a–f`
- 2 hex characters = 1 byte (8 bits)
- Commonly used to display binary data in readable form

### Example
48656c6c6f
Decoded result: Hello


Base64 is **not encryption**.

---

## Encoding vs Encryption vs Hashing

| Type | Purpose | Reversible | Examples |
|----|----|----|----|
| Encoding | Data representation | Yes | Hex, Base64 |
| Encryption | Data protection | Yes (with key) | XOR, AES |
| Hashing | Data integrity | No | MD5, SHA-256 |

---

## CryptoPals Rule (Important)
> Always operate on raw bytes, never on encoded strings.  
> Only use hex and base64 for pretty-printing.

### Meaning
- Hex and Base64 are only representations
- Cryptographic operations must be performed on raw byte data
- Incorrect handling of encodings can cause bugs and security issues

---
