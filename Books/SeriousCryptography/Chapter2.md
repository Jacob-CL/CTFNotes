# Randomness
- Strictly speaking, there is no such thing as a series of random bits. What IS random is the algo, or process that produces the random bits. So when we say 'random bits' we actually mean randomly generated bits.
- 00000000 or something like 11011000 BOTH have an equal chance of being randomly generated (given high entropy)
- Two common errors:
  - Mistaking nonrandomness for randomness: Thinking that an object was randomly generated simply because it looks random
  - Mistaking randomness for nonrandomness: Thinking that patterns appearing by chance are there for a reason other than chance
  - There's a big difference between random-looking and actually random.
- Any randomized process is characterized / defined by a **probability distribution**
  - A distribution lists the outcomes of a randomized process where each outcome is assigned a probability.
  - A probability measures the likelihood of an event occuring. It's expressed as a real number between 0 and 1. Where 0 = no chance, and 1 = every chance but must include all possible outcomes.
  - A uniform distribution occurs when all probabilities in the distribution are equal, meaning that all outcomes are equally likely to occur.
  - A non-uniform distribution is where the distribution is not equal, e.g weighted/loaded dice
- **Entropy** is the measure of uncertainty, or disorder, in a system. The higher the entropy, the less certainty found in the result of a randomized process.
  - High entropy is good for crypto.
  - Entropy is maximized when the distribution is uniform because a uniform distribution maximizes uncertainty: no outcome is more likely than any other. Just as when the distribtionis not uniform, entropy is lower.
  - Entropy can also be viewed as a measure of information. The result of a fair coin toss = 1 bit of information (heads or tails) and you're unable to predict in advance the result. In an unfair coin toss, you can so the result of the unfair coin toss gives you the info needed to predict the result with certainty.
- **Random and Pseudorandom Number Generators** are components of computers tha return random bits when requested to do so.
  - To do this, you need 2 things: a source of entropy (provided by RNGs) and/or cryptographic algos that produce high quality random bits (found in PRNGs) but using both RNGs and PRNGs is the key to making cryptography practical and secure.
  - For **RNGs** randomness comes from the environment (leverage analog entropy like temperature, air pressure to produce unpredictable bits in a digital system.) but sometimes can be difficult to estimate the entropy of these environment factors to generate entropy. They can also harvest the entropy in a running OS by drawing from attached sensors, I/O devices, network or disk activity, running process, mouse movements etc
  - Such system- and human-generated activities can be a good source of entropy, but they can be fragile and manipulated by an attacker. Also, they’re slow to yield random bits.
  - Such a thing as QRNG which is a type of RNG that relies on the randomness arising from quantum mechanical phenomena such as radioactive decay, photon polirazation or thermal noise.
  - For **PRNG**, they address the challenge in generating randmonness by reliably producing many artificial random bits from a few true random bits. e.g an RNG system that translates mouse movements to random bits would stop working if you stopped moving the mouse, whereas a PRNG always returns pseudorandom bits when requested to do so.
  - PRNG rely RNGs but behave differently.. RNGs produce random bits relatively slowly from analog sources, in a non-deterministic way, and with no guarantee of uniform distribution or of high entropy. In contrast, PRNGs produce random-looking bits quickly from digital sources, in a deterministic way, uniformly distributed, and with an entropy guaranteed to be high enough for cryptography.
  - Essentially, PRNGs transform a few unreliable random bits into long term stream of reliable pseudorandom bits suitable for crypto applications.
 
## How do PRNGs work?
- PRNG receives random bits from RNG at regular intervals and uses them to update the contents of a large memory buffer, called the entropy pool. The entropy pool is the PRNGs source of entropy, just like the physical environment is for RNGs.
- Then, the PRNG runs a deterministic random bit generator (DRBG) algorithm that expands some bits from the entropy pool into a much longer sequence.
- DRBG is DETERMINISTIC, not randomized. Given one input, you will always get the same output. The PRNG ensures that it's DRBG never receives the same input twice so it can generate unique pseudorandom sequences.
- In the course of its work, the PRNG performs three operations:
  - `init()` Initializes the entropy pool and the internal state of the PRNG. The init operation resets the PRNG to a fresh state, reinitializes the entropy pool to some default value, and initializes any variables or memory buffers used by the PRNG to carry out the refresh and next operations. 
  - `refresh(R)` Updates the entropy pool using some data, R, usually sourced from an RNG. The refresh operation is often called reseeding, and its argument R is called a seed. When no RNG is available, seeds may be unique values hardcoded in a system. The refresh operation is typically called by the operating system, whereas next is typically called or
requested by applications.
  - `next(N)` Returns N pseudorandom bits and updates the entropy pool. The next operation runs the DRBG and modifies the entropy pool to ensure that the next call will yield different pseudorandom bits.

## PRNG Fortuna
- Fortuna is a PRNG used in Windows, which superseded Yarrow.
- Doesn't include a comprehensive test suite to check that an implementation is correct, which makes it difficult to ensure that your implementation of Fortuna will behave as expected.
- Fortuna might not notice if the RNGs fail to produce enough random bits, and as a result will produce lower-quality pseudorandom bits, or it may stop delivering pseodurandom bits altogether.
- Exposing associated seed files to attackers. The data in Fortuna seed files is used to feed entropy to Fortuna through refresh calls when an RNG is not immediately available, like immediately after a reboot and before the system's RNG have recorded any unpredictable events.
- Fortuna will produce the same bit sequence twice. Seed files should be therefore be erased after use to ensure they aren't used.

## Cryptography vs. Noncryptographic PRNGs
- Noncrypto PRNGs are designed to produce uniform distributions for applications such as scientific simulations or video games. However, you should never use noncrypto PRNGs in crypto applications, because they're insecure; they're concerned only with the quality of the bits' probability distribution and not with their predictability.
- Crypto PRNGs are unpredictable because they're also concerned with the strength of the underlying operations used to deliver well-distributed bits.
- Most PRNGs exposed by programming languages are noncryptographic.
- Popular Noncrypto PRNG: **Mersenne Twister**. It generates uniformly distributed random bits without statistical bias, but it's predictable: given a few bits produced by MT, one can guess which bits will follow.

## Linearity Insecurity
- An XOR combination of bits is called a linear combination
