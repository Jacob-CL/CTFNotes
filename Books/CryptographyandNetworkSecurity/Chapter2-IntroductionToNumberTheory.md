# Chapter 2: Introduction to Number Theory
Number theory is everywhere in cryptographic alogrithms and are fundamental to asymmetric (public-key) cryptographic algorithms.

## 2.1 Divisibility and the Division Alogrithm
### Divisibility:

When we say `b` divides `a` (written as `b|a`), we mean: You can divide `a` by `b` and get a whole number with no leftover.
- 3 divides 12 because `12 ÷ 3 = 4` (no remainder) → We write this as `3|12`
- 5 divides 30 because `30 ÷ 5 = 6` (no remainder) → We write this as `5|30`
- 4 does NOT divide 15 because `15 ÷ 4 = 3` remainder 3 → We write this as `4∤15` (the crossed-out | means "does not divide")

If you wanted to find all divisors for the number `24`:
- 1 goes into 24 (24 times)
- 2 goes into 24 (12 times)
- 3 goes into 24 (8 times)
- 4 goes into 24 (6 times)
- 5 does not go in to 24

IMPORTANT NOTE: The Divisibility Statement vs. Actual Division:
`7|14` is NOT an equation that equals something. It's a statement that means "7 divides 14" - and this statement is either TRUE or FALSE. 7|14 = TRUE (because 7 does divide 14 evenly)

For Actual Division:
When you want to find the result of division, you use the division symbol `÷`: `14 ÷ 7 = 2`  (This gives you the quotient)

Therefore, 
- `7|14` means `7 divides 14` → This is a TRUE statement
- `14|7` means `14 divides 7` → This is a FALSE statement (because `7 ÷ 14 = 0.5`, not a whole number)
- `14 ÷ 7 = 2` → This gives you the actual result of division
- `7 ÷ 14 = 0.5` → This gives you the actual result of division

The vertical bar `|` is about whether division works cleanly, while ÷ is about what you get from division.

So we have some simple rules of divisibility:
- If something divides 1, it must be 1 or -1 because only they can divide 1 evenly.
- If `a` divides `b` AND `b` divides `a`, then they're basically the same size. Like saying 6 divides 12 AND 12 divides 6 - this only works if they're euqal (or opposites)
- Any number divides 0: `0|anything = 0` so there's never a remainder
- `Chain rule`: if `a` divides `b`, and `b` divides `c` then `a` divides `c`: e.g `11(a)|66(b)` --> `66(b)|198(c)` --> then 11(a) MUST | by 198(c)
- `Combination Rule`: If `b|g` AND `b|h`, then `b|(mg + nh)` where `m` and `n` are ANY integers. e.g If `7|14` and `7|63`, then 7 will also divide expressions like `(3×14 + 2×63), (5×14 - 4×63)`, `(-1×14 + 10×63)` etc.

To explain the combination rule more:
`7| both 14 AND 63` so we can say that the total of (ANY arbitrary number x 14 + ANY arbitrary number x 63) will be divisable by 7. e.g
```
(1×14 + 1×63) = 77 ✓ (77 ÷ 7 = 11)
(5×14 + 3×63) = 259 ✓ (259 ÷ 7 = 37)
(10×14 - 4×63) = -112 ✓ (-112 ÷ 7 = -16)
```
The coefficents can be any integer you want

### The Division Algorithm:
- Positive integers: 1, 2, 3, 4, 5, ... (greater than 0)
- Nonnegative integers: 0, 1, 2, 3, 4, 5, ... (greater than or equal to 0)

The Division Algorithm is simply a formal way to describe what happens when you divide any integer by a positive integer. Here's the simple explanation:

When you divide any integer `a` by any positive integer `n`, you always get:
- A quotient `q` (how many times n goes into a)
- A remainder `r` (what's left over)

The formula is `a = qn + r` where the remainder `r` must satisfy: `0 ≤ r < n`

#### TL;DR
Any number equals (some whole number times the divisor) plus a remainder that's always smaller than the divisor
Positive example: `11 ÷ 7`
```
11 = (1 × 7) + 4
Quotient q = 1, Remainder r = 4
Check: 4 < 7 ✓
```
Negative example: `-11 ÷ 7`
```
-11 = (-2 × 7) + 3
Quotient q = -2, Remainder r = 3
Check: 3 < 7 ✓ (remainder is still positive!)
```
The remainder is always non-negative and always smaller than the divisor, even when dividing negative numbers. This is what makes the algorithm "work" consistently. This guarantees that every division has a unique quotient and remainder, which is fundamental for number theory, computer science, and many mathematical proofs.

### 2.2 The Euclid Algorithm
- The Euclidean Algorithm is a simple way to find the Greatest Common Divisor (GCD) of two numbers. The basic idea is that instead of listing all factors, you use **repeated division** and focus on the **remainders**.
- One of the basic techniques of number theory is the Euclidean Algorithm, which is a simple procedure for determining the greatest common divisor of two positive integers. First, we need a simple definition: Two integers are **relatively prime** if and only if their only common positive integer factor is 1.

The process:
1. Divide the larger number by the smaller number
1. Look at the remainder
1. Replace the larger number with the smaller number, and the smaller number with the remainder
1. Repeat until the remainder is 0
1. The last non-zero remainder is your GCD!

Simple Example: Find GCD(710, 310)
- Step 1: `710 ÷ 310 = 2` remainder `90`
  - So: `710 = 2 × 310 + 90`
- Step 2: `310 ÷ 90 = 3` remainder `40`
  - So: `310 = 3 × 90 + 40`
- Step 3: `90 ÷ 40 = 2` remainder `10`
  - So: `90 = 2 × 40 + 10`
- Step 4: `40 ÷ 10 = 4` remainder `0`
  - So: `40 = 4 × 10 + 0`
Since remainder = `0`, we STOP! Answer: `GCD(710, 310) = 10` Therefore, keep dividing and using remainders, the remainders get smaller and smaller and eventually you hit `0`, the step before 0 gives you the GCD.

### 2.3 Modular Arithmetic
Modular Arithmetic is basically "clock arithmetic" - it's about what happens when numbers "wrap around" after reaching a certain point.
- `a mod n` = the remainder when you divide `a` by `n`
Examples:
- `17 mod 12 = 5` (because 17 ÷ 12 = 1 remainder 5)
- `25 mod 7 = 4` (because 25 ÷ 7 = 3 remainder 4)
- `10 mod 3 = 1` (because 10 ÷ 3 = 3 remainder 1)

`a ≡ b (mod n)` means `a` and `b` have the same remainder when divided by `n`
Examples:
- `17 ≡ 5 (mod 12)` because both 17 and 5 give remainder 5 when divided by 12
- `25 ≡ 4 (mod 7)` because both 25 and 4 give remainder 4 when divided by 7

Real-World Examples:
- Days of the week (mod `7`):
- Today is Tuesday (day `2`)
What day is it 10 days from now?
- `2 + 10 = 12`
- `12 mod 7 = 5` → Friday!

### 2.4 Prime Numbers
A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself. (Except 1)
- Prime: 2, 3, 5, 7, 11, 13, 17, 19, 23... (2 is the only even prime number)
- Not Prime: 4 (divisible by 2), 6 (divisible by 2 and 3), 9 (divisible by 3)
- There are infinite number of primes (proven by Euclid)

The Fundamental Theorem of Arithmetic is that every number can be broken down into prime factors in exactly one way, think of it like: every number has a unique "DNA" made of primes:
- `12 = 2² × 3`
- `30 = 2 × 3 × 5`
- `100 = 2² × 5²`

Relatively Prime (Coprime) are two numbers which are "relatively prime" if their only common factor is 1
- `8` and `15` are relatively prime (even though 8 isn't prime)
- `GCD(8, 15) = 1`

Prime Factorization is breaking numbers into their prime building blocks:
- `60 = 2² × 3 × 5`
- `84 = 2² × 3 × 7`

Cryptography / hash functions relies on the difficulty of factoring huge numbers e.g RSA encryption uses very large prime numbers.

### 2.5 Fermat's and Euler's Theorems
These 2 theorems play an important rtole in public-key cryptography.

Fermat Last Thereom: You can’t take three whole numbers (like 3, 4, and 5), raise them to a power greater than 2, and have them fit nicely into the equation: a^n + b&^n = c^n (Pythag theorem) unless n = 2.
- e.g `3^2 + 4^2 = 5^2 | 9 + 16 = 25` But if it were to the power of 3 or any other number, then it wouldnt work.

Euler's Totient Function: How many numbers less than n are coprime to n. Super important to RSA
- e.g `φ(9) = 6` Because the numbers 1, 2, 4, 5, 7, 8 are all coprime to 9.
- Remember: Coprime numbers, also known as relatively prime or mutually prime numbers, are two or more integers that share no common factors other than 1. In other words, their greatest common divisor (GCD) is 1. For example, 8 and 9 are coprime because their only common factor is 1, even though neither is a prime number.

Euler's Thereom: `aϕ(n) ≡ 1 (mod n)` <-- the foundation of RSA encryption
- If two numbers `a` and `n` share no common factors (are 'coprime') then  `aϕ(n) ≡ 1 (mod n)`
- The theorem guarantees that encryption followed by decryption returns the original message.

### 2.6 Testing for Primality
- For many cryptographic algorithms, it is necessary to select one or more very large prime numbers at random. Thus, we are faced with the task of determining whether a given large number is prime. There is no simple yet efficient means of accomplishing this task. 
- The Miller-Rabin Algorithm yields a number not necessarily a prime but one that is almsot certianly a prime. It's typically used to test a large number for primality. Therefore, it's a fast-way to check if a number is prime but won't 100% gurantee it
- Used to generate big prime numbers for things like RSA keys
Miller-Rabin super simplified:
1. Pick a number you want to test — let’s call it n.
2. Choose a random number a (called a "witness").
3. Do some math magic using modular arithmetic.
4. If the result shows something weird, n is definitely not prime.
5. If everything looks normal, n might be prime — so you test again with a different a.
Do this a few times, and if n passes every test, you can be pretty confident it’s prime. Essentially it's looking for some evidence of the number NOT being prime rather THAN prime since it's much easier to find evidence of the former. Instead of proving a number is prime (which is hard and slow), it tries to find evidence that it’s not — because that’s much faster.

### 2.7 The Chinese Remainder Thereom (CRT)
- Basically says that it's possible to reconstruct (find) integers in a certain range from their clues or 'residues modulo (a set of pairwise relatively prime moduli)'
- So rather than being told a number, you're given clues about it's modulo, and can then guess the number from that.

<img width="761" height="318" alt="image" src="https://github.com/user-attachments/assets/7dfce00e-29ae-4b71-be13-afa18682c281" />








  
