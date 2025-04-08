# Known Plaintext Attack on Hill Cipher

## What is it?

A Known Plaintext Attack (KPA) allows an attacker to recover the encryption key if they know both:
- A piece of the original plaintext
- Its corresponding ciphertext

In the Hill Cipher, encryption is defined as:

C = K * P mod 26

Where:
- `K` is the secret key matrix
- `P` is the plaintext matrix
- `C` is the ciphertext matrix

To recover `K`, we reverse this:

K = C * P⁻¹ mod 26

This requires `P` to be square and invertible mod 26.

---

## Code Walkthrough

### 1. Define Helper Functions
- Convert between text and numeric values (A=0, ..., Z=25)
- Invert matrices modulo 26 using SymPy

### 2. Encrypt a Known Plaintext
We use a 2x2 key matrix to encrypt a 4-letter plaintext (e.g., "HELP"). The ciphertext is produced using matrix multiplication modulo 26.

### 3. Perform the Attack
We:
- Convert known plaintext and ciphertext into 2x2 matrices
- Compute the inverse of the plaintext matrix
- Multiply the ciphertext matrix by the inverse to recover the original key

---

## Summary

With just a few known plaintext-ciphertext pairs, the Hill cipher can be broken if the attacker can build a square, invertible matrix. This demonstrates the **importance of using modern cryptography** with semantic security guarantees.

