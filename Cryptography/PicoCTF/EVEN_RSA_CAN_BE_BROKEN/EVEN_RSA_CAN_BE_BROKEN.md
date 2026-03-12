# EVEN RSA CAN BE BROKEN

## Vulnerability
The `get_primes` function generates **even "primes"**, meaning one of p or q is likely **2**.

If `p = 2`, then `q = N // 2`, and we can recover the private key `d` and decrypt.

## Solver Script
```python
from Crypto.Util.number import inverse, long_to_bytes

N = 22764400623309359492135866343681545944755719029422476642508558978400937373533452326250957527581638834621797130306521074447974539684712703010941071565199038
e = 65537
c = 19105010402268421445229472258700264624961255251550411275745770531997589653356191171475557464456426369452499663337183167395195672737961516233762476199869191

# If p = 2
p = 2
q = N // 2

assert p * q == N, "p=2 didn't work"

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, N)
print(long_to_bytes(m).decode())
```

Answer: `picoCTF{tw0_1$_pr!m3de643ad5}`

---

# RSA — Core Concepts & CTF Attack Thinking

## What is RSA?

RSA is a public-key encryption algorithm. It relies on the mathematical difficulty of **factoring large numbers**.

### The Key Variables

| Variable | Name | What it is |
|----------|------|------------|
| `p`, `q` | Primes | Two large, secret, randomly chosen prime numbers |
| `N` | Modulus | `p × q` — made public, used to encrypt and decrypt |
| `e` | Public exponent | Almost always `65537` — made public |
| `d` | Private exponent | Computed from p, q, and e — kept secret |

### How N is Used

- **Encryption:** `ciphertext = message^e mod N`
- **Decryption:** `message = ciphertext^d mod N`

N is public — anyone can see it. But to compute `d` (the decryption key), you need to know `p` and `q`. And finding `p` and `q` from `N` alone (factoring) is computationally infeasible when they are large random primes — this is the entire basis of RSA's security.

---

## Why Even Primes Break RSA

All primes except 2 are odd. If `get_primes` returns an even number, one of p or q is almost certainly **2**.

If `p = 2`:
```
N = 2 × q
```

Factoring N is now trivial — just divide by 2:
```python
q = N // 2  # instant, one operation
```

It doesn't matter how large N is. The hard problem disappears completely.

### Concrete Example
```
N = 38
q = 38 // 2 = 19
# p = 2, q = 19 — done
```

Once you have p and q, you can compute d and decrypt anything:
```python
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
message = pow(ciphertext, d, N)
```

---

## CTF Thought Process for RSA Challenges

### 1. Read the source code critically
Look for **what's missing**. Hidden imports or helper functions are almost always where the vulnerability lives.
```python
from setup import get_primes  # setup.py not provided — suspicious
```

### 2. Run through the RSA attack checklist
Ask yourself: what could go wrong with RSA?

- [ ] Is p or q too small?
- [ ] Are p and q too close together? (Fermat's factorization attack)
- [ ] Is p or q even? (trivial factorization)
- [ ] Is e tiny? (small exponent attack)
- [ ] Is N reused across encryptions with related messages? (common modulus attack)

### 3. Use the challenge name as a hint
CTF authors almost always embed the vulnerability in the title.
- "EVEN RSA CAN BE BROKEN" → even → p or q is literally even

### 4. Test your hypothesis cheaply before solving
```python
print(N % 2)  # If 0, N is even → p or q = 2
```

### 5. Then write the full solver

---

## For RSA to Be Secure, Primes Must Be:
- **Large** — so brute force fails
- **Odd** — all primes except 2 are odd; 2 makes N trivially factorable
- **Random** — so patterns can't be exploited
