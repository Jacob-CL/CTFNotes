# Cryptographic Security
- The main difference betwen software security and cryptographic security is that we can quanitfy the latter. It's possible to calculate the amount of effort required to break a cryptographic algorithm. 
- 2 notions define the concept of impossible in cryptography: `unconditional security` and `computational security`
- `Unconditional security` is about theorectical impossibility. It's based not on how hard it is to break a cipher but on whether it's conceivable to break at all. A cipher is unconditonally secure only if given unlimited computation time and memory, it cannot be broken. If infinite compute can't solve it then it's unconditionally secure (OTP). If it take's a million years, it's unconditionally insecure.
- `Computational security` is about practical impossibility. Computational security views a cipher as secure if it cannot be broken within a reasonable amount of time and with reasonable resources such as memory, hardware, budget, and energy. Computational security is a way to quantify the security of a cipher or any crypto algo. A cipher is computationally secure if it takes 1 millio nyears to break, becqause it's practically impossible to break.

<img width="907" height="138" alt="image" src="https://github.com/user-attachments/assets/1d24ab40-c327-4116-8c03-db8131a84aa1" />

- Consider a symmetric cipher with a 128bit key. Ideally, this cipher should be `(t, t/2**128)`- secure for any value of `t` between 1 and 2**128. The best attack should be brute force. Any better attack would have to exploit some imperfection in the ciopher, so we strive to create ciphers where brute force is the best possible attack. The key thus needs to be long enough to blunt brute-force attacks in practice. Also note that computational security is technology agnostic, which means a cipher that's `(t, e)`-secure today, will be `(t, e)` secure tomorrow.

## Quantifying Security
- When you've found an attack, you should first figure out how efficient it is in theory and how practical it is if at all. Similar if given a cipher that's allegedly secure, you'll want to know what amount of work it can withstand.

### Measuring Security in Bits
- Expresses the cost of the fastest attack against a cipher by estimating the order of magnitude of the number of operations it needs to succeed. Unfortunately, it only focuses on the time it takes to perform an attack.
- In computationally security, a cipher is `t`-secure when a successful attack needs at least `t` operations.
- Two ciphers with the same bit security level can therefore have vastly different real-world security levels when you factor in the actual cost of an attack to a real attacker.
- Say we have two ciphers, each with a 128-bit key and 128-bit security. We must evaluate each cipher 2128 times to break it, but the second cipher is 100 times slower than the first.Evaluating the second cipher 2**128 times thus takes the same time as 100 x 2**128 = 2**134.64 evaluations of the first. If we count in terms of the first, fast cipher, then breaking the slower one takes 2**134.64 operations. If we count in terms of the second, slow cipher, it takes only 2128 operations. Should we then say that the second cipher is stronger than the first? In principle, yes, but we rarely see such a hundred-fold performance difference between common ciphers.
- Bit security proves useful when comparing the security level of ciphers, but it doest provide enough info on the actual cost of an attack. It's almost too simple an abstraction 
- If you know approx. how many operations it takes to break a cipher, you can determine it's security level in bits by taking the binary logarith, of the number of operations: if it takes 1mil operations, the security level is log2(1000000) or about 20 bits (as 1mil is approx = 2**20)
- Recall that an n-bit key will give at most n-bit security because a brute-force attack with all 2**n possible jeys will aways succeed. But the key size doesn't always match the security level - it just gives an upper bound or the highest possible security level.

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
