# Cryptographic Security
- The main difference betwen software security and cryptographic security is that we can quanitfy the latter. It's possible to calculate the amount of effort required to break a cryptographic algorithm. 
- 2 notions define the concept of impossible in cryptography: `unconditional security` and `computational security`
- `Unconditional security` is about theorectical impossibility. It's based not on how hard it is to break a cipher but on whether it's conceivable to break at all. A cipher is unconditonally secure only if given unlimited computation time and memory, it cannot be broken. If infinite compute can't solve it then it's unconditionally secure (OTP). If it take's a million years, it's unconditionally insecure.
- `Computational security` is about practical impossibility. Computational security views a cipher as secure if it cannot be broken within a reasonable amount of time and with reasonable resources such as memory, hardware, budget, and energy. Computational security is a way to quantify the security of a cipher or any crypto algo. A cipher is computationally secure if it takes 1 millio nyears to break, becqause it's practically impossible to break.

<img width="907" height="138" alt="image" src="https://github.com/user-attachments/assets/1d24ab40-c327-4116-8c03-db8131a84aa1" />

- Consider a symmetric cipher with a 128bit key. Ideally, this cipher should be `(t, t/2**128)`- secure for any value of `t` between 1 and 2**128. The best attack should be brute force. Any better attack would have to exploit some imperfection in the cipher, so we strive to create ciphers where brute force is the best possible attack. The key thus needs to be long enough to blunt brute-force attacks in practice. Also note that computational security is technology agnostic, which means a cipher that's `(t, e)`-secure today, will be `(t, e)` secure tomorrow.

## Quantifying Security
- When you've found an attack or a cipher, you should first figure out how efficient it is in theory and how practical it is if at all.

### Measuring Security in Bits
- Bit security expresses the computational cost of the fastest known attack against a cipher, measured as the base-2 logarithm of the number of operations required. For example, if an attack needs NNN operations, the security level is log⁡2(N)\log_2(N)log2​(N) bits.
- What it captures: Bit security focuses on the number of operations, not the time per operation. It is an abstraction that ignores implementation speed, hardware differences, and parallelization.
- Suppose two ciphers both require 21282^{128}2128 operations to break (128-bit security). If Cipher A is fast and Cipher B is 100× slower per operation, then: Breaking Cipher B takes 100× more time in practice. In terms of Cipher A’s speed, that’s equivalent to 100×2128≈2134.64100 \times 2^{128} \approx 2^{134.64}100×2128≈2134.64 operations.
Important: Bit security does not adjust for speed differences. Both ciphers are still considered 128-bit secure in theory.
- Limitations: Bit security is useful for comparing algorithms but oversimplifies real-world attack costs. It ignores:
    Hardware acceleration
    Memory requirements
    Parallelization
    Energy consumption

Calculating bit security:
- If an attack requires 1,000,000 operations:
- log⁡2(1,000,000)≈20 bits.\log_2(1{,}000{,}000) \approx 20 \text{ bits.}log2​(1,000,000)≈20 bits.

Key size vs. security:
- An nnn-bit key provides at most nnn-bit security because brute force over 2n2^n2n keys will succeed. However:

Actual security may be lower due to weaknesses.
- Example: DES uses a 56-bit key but is breakable with fewer than 2562^{56}256 operations due to known attacks.

## Calculating the full attack cost
There are other factors to take into account when estimating the actual security level:
- `Parallelism` - The ability of the attack's implementation to take advantage of parallel computing such as multicore systems. Algorithms that become `N` times faster to attack when N cores are available are embarrassingly parallel; their execution times scale linearly with respect to the number of computing cores.
- `Memory` - We eval cryptanalytic attacks with respect to their use of time and space: How many operations do the perform over time, how much memory or space do they consume, how do they use the space they consume and what is the speed of the available memory. It's important to consider how many memory lookups the attack requires, the speed of memory accesses (which may differ between reads and writes), the size of the accessed data, the access pattern (contiguous or random memory addresses), and how it structures data in memory.
- `Precomputation` - Precomp operations need to be performed only once and can be reused over subsequent executions of the attack. Sometimes called `offline stage` of an attack. Consider the time-memory trade-off attack, in which the attacker performs one huge computation that produces large lookup tables that we then store and reuse to perform the actual attack. For example, one attack on 2G mobile encryption took two months to build 2TB’s worth of tables, which attackers then used to break the encryption in 2G and recover a secret session key in only a few seconds.
- `Number of targets` - The greater the number of targets, the greater the attack surface, and the more attackers can learn about the keys they’re after. A bruteforce key search - rather than brute 1 key, you brute many at once, the chances are greater than 1 will break before the others.

## Choosing and Evaluatiing Security Levels
- There will be times when a security level lower than 128 bits is justified such as when you need security for a short time period and when the costs of implementing a higher security level will negatively impact the cost or usability of a system. An example is pay-TV systems, wherein encryption keys are either 48 or 64 bits. This sounds ridiculously low but is sufficient because the key refreshes every 5 or 10 seconds.
- The difference between 80 bits and 128 bits of key search is like the difference between a mission to Mars and a mission to Alpha Centauri. As far as I can see, there is no meaningful difference between 192-bit and 256-bit keys in terms of practical brute-force attacks; impossible is impossible.

## Acheiving Security
How to be confident with your chosen Crypto scheme? You want provable security (mathematical proofs) or evidence of failed attempts to break the algo (heuristic / probable security)
- `Provable Security`:
- `Heuristic Security`:
