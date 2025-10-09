# Chapter 4 - Block Ciphers and the Data Encryption Standard
## 4.1 Traditional Block Cipher Structure
- Many important symmetric block encryption algos use a structure referred to as a Feistel block cipher.

### Stream Ciphers and Block Ciphers
- A stream cipher is one that encrypts a digital data stream one bit or one byte at a time.
- A block cipher is one in which a block of plaintext is treated as a whole and used to produce a cipherblock of equal length.
- Blocksizes of 64 or 128 are typically used
- In both cases (stream or block) the two users need to share a symmetric encryption key.
- There are some modes of operation where a block cipher can be used to achieve the same effect as a stream cipher
- In general, block ciphers  seem more applicable to a broader range of applications than stream ciphers. The vast majority of network-based symmetric cryptographic applications make use of block ciphers.

### Motivation for the Ferstel Cipher Structure
- An arbitrary reversible substitution cipher (the ideal block cipher) for a large block size is not practical, however, from an implementation and performance point of view. For such a transformation, the mapping itself constitutes the key.
- A block cipher operates on a plaintext block of `n` bits to produce a ciphertext block of `n` bits. There are `2^n` possible different plaintext blocks and, for the encryption to be reversible (i.e for decryption to be possible), each must produce a unique ciphertext block.
- A 4-bit input produces one of 16 possible input states, which is mapped by the substitution cipher for n = 4. A 4-bit input produces one of 16 possible input states, which is mapped by the substituion cupher into a unique one of 16 possible output states, each of which is represdented by 4 ciphertext bits.
- Feistel refers to a block cipher that can be used to define any reversible mapping between plaintext and ciphertext as the ideal block cipher because it allows for the maximum number of possible encryption mappings from the plaintext block.
- Problem with this though, that if the block size is small (like `n = 4`) then system is essentially a substitution cipher. And this is vulnerable to frequency analysis etc. Therefore, it's not the substitution cipher that's weak it's the small block size. If `n` is sufficiently large then the arbitary reversible substitution between plaintext and ciphertext, then the statistical characteristics of the source plaintext are masked to such an extent that this type of cryptanalysis is infeasible.
- An arbitrary reversible substitution cipher (the ideal block cipher) for a large block size is not practical, however, from an implementation and performance point of view. For such a transformation, the mapping itself constitutes the key.
- Feistal proposed the use of a cipher that alternates substitutions and permutations, where these terms are defined as:
- Substitution: Each plaintext element or group of elements is uniquely replaced by a coressponding ciphertext element or group of elements
- Permutation: A sequence of plaintext elements is replaced by a permutation of that sequence. That is, no elements are added or deleted or replaced in the sequence, rather the order in which the elements appear in the sequence is changed.
