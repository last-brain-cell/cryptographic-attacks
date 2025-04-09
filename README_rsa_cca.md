# Chosen Ciphertext Attack (CCA) on RSA

## What is it?

In a Chosen Ciphertext Attack, the attacker:
1. Intercepts a ciphertext `c`
2. Modifies it to `c' = (s^e * c) mod n` (for some known `s`)
3. Submits `c'` to a decryption oracle
4. Gets back `m' = (s * m) mod n`
5. Recovers `m = m' * s⁻¹ mod n`

This attack works because RSA is **multiplicatively homomorphic**:

Enc(m1) * Enc(m2) = Enc(m1 * m2)

---

## Code Walkthrough

### 1. Key Generation
- Generate small random primes `p` and `q`
- Compute `n = pq`, `φ(n) = (p-1)(q-1)`
- Choose `e = 3` and ensure `gcd(e, φ) = 1`
- Compute private key `d = e⁻¹ mod φ(n)`

### 2. Encrypt a Message
A test message like `"OK"` is converted to a number and encrypted with RSA.

### 3. Perform the CCA
- Attacker picks a random `s`
- Computes `c' = (s^e * c) mod n` and sends to decrypt
- Multiplies result by `s⁻¹ mod n` to recover `m`

---

## Summary

This demonstrates how **basic RSA without padding** is vulnerable to CCA. In real systems, padding schemes like **OAEP** are used to prevent this type of attack.
