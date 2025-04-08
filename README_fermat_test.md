# Fermat Primality Test

## What is it?

The Fermat Primality Test is a **probabilistic** method to check whether a number is likely prime, based on Fermat’s Little Theorem:

If n is prime, then for any a < n: a^(n-1) ≡ 1 mod n

If this doesn’t hold for some base `a`, `n` is definitely **composite`.

---

## Code Walkthrough

### 1. Randomized Test
We select a random base `a ∈ [2, n-2]` and compute:

pow(a, n-1, n)

If the result ≠ 1 for any `a`, the number is composite.

We repeat this `k` times (e.g. `k=5`) for greater confidence.

### 2. Run Test on Sample Numbers
We run the test on:
- Prime numbers like 13, 17, 97
- Composite numbers like 15, 21
- A **Carmichael number** like 561, which fools Fermat's test

---

## Summary

This test is fast and good for **initial filtering**, but it can be fooled by Carmichael numbers. More reliable tests (like Miller-Rabin) are used in practice for cryptographic key generation.
