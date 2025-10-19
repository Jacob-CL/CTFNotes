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

