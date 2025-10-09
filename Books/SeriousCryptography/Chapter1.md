# Chapter 1 - Encryption
- Encryption is the principal application of cryptography; it makes data incomprehensible to ensure its confidentiality. Encryption uses an algo called a cipher and a secret value called a key. If you don't know the secret key, you can't decrypt, nor can you learn any bit of informatio on the encrypted message - neither can any attacker.
- This chapter focuses on symmetric encryption, where the decryption key = encryption key (Unoike asymmetric or public-key encryption)

## The Basics
The term 'cipher' = 'encryption'
- `P` plaintext
- `K` key
- `C` ciphertext

For some ciphers, the ciphertext is the same size as the plaintext; for others, the ciphertext is slightly larger/longer. However, ciphertexts can never be shorter than plaintexts.

### Classical ciphers 
Predate computers and work on letters or words rather than on bits, making them much simpler.
- Caesar
- Vignere - Used during the American Civil War by Confederate forces and during WW1 by the Swiss Army among others. Similar to the Caesar cipher, except that letters aren't shifted 3 places but rather by values defined by a key, a collection letters that represent numbers based on their position in the alphabet. e.g if the key (secret word) is DUH, letters in the plaintext are shifted using the values 3, 20, 7 because D is three letters after A, U is 20 letters after A, and H is seven letters after A. The 3, 20, 7 pattern repeats until you've encrypted the entire plaintext. CRYPTO would encrypt to FLFSNV using DUH as the key. Spaces are usually removed from Vignere ciphertexts to hide word boundaries.
  - Vignere is weak to repeated patterns every X number of positions. Notice that in the ciphertext WBLBXYLHRWBLWYH, the group of three letters WBL appears twice in the ciphertext at nine-letter intervals. This suggests that the same three-letter word was encrypted using the same shift values, producing WBL each time. A cryptanalyst can then deduce that the key’s length is either nine or a value that divides nine (that is, three). Then use frequency analysis. 

### How ciphers work
We can abstract out the workings of a cipher by identifying its two main components: 
- A permutation and a mode of operation. A permutation is a function that transforms an item (in crypto, a letter or a group of bits) such that each item has a unique inverse. 
- A mode of operation is an algo that uses a permutation to process messages of arbitrary size.

### The Permutation
- Classical ciphers work by replacing each letter with another (substitution) In Caesar or Vignere, the substituion is a shift in the alphabet, although the alphabet or set of symbols can vary. (English alphabet or Arabic?)
- A cipher's substitution can't jsut be any substituion. It should be a permutation, which is a rearrangement of the letters A -> Z, such that each letter has a unique inverse. For example, a substitution that transforms the letters A, B, C and D respectively to, C, A,  D, and B is a permutation.
- However, a substitution that transforms A, B, C, D to D, A, A, C is NOT a permutation because both B and C map into A. With a permutation, each letter has exactly one inverse.

Still, not every permutation is secure. To be secure, a cipher's permutation should satisfy 3 criteria:
- The permutation should be determined by the key: As long as the key is a secret, then so is the permutation.
- Different keys should result in different permutations: if different keys result in identical permutations, that means there are fewer distinct keys than permutations and therefore fewer possibilites to try when decrypting without the key.
- The permutation should look random, loosely speaking: There should be no pattern in the ciphertext after performing a permutation, because patterns make a permutation predictable for an attacker and therefore less secure.

We'll call a permutation that satisfies these criteria a secure permutation. A secure permutation is necessary but insiffucient on it's own for building a secure cipher.

### The Mode of Operation
- If we have A -> X, B -> M and N -> L, then BANANA = MXLXLX, where each occurence of A is replaced by an X. Using the same permutation for all letters in the plaintext thus reveals any and all duplicate letters. Frequency analysis will help reveal what these duplicate letters are. 
- The mode of operation (or mode) of a cipher mitigates the exposure of duplicate letters in the plaintext by using different permutations for duplicate letters. The mode of the Vignere cipher partically addresses this; if they key is N letters long, then N different permutations will be used for every N consecutive letter. However, this can still result in patterns in the ciphertext because every Nth letter of the message uses the same permutation. That’s why frequency analysis works to break the Vigenère cipher.

### Why Classical Ciphers are insecure
- Classical ciphers are doomed to be insecure because they're limited to operations you can do in your head or on a piece of paper.
- Remeber that a cipher's permutation should look random to be secure. Of course, the best way to look random is to BE random. 
- ! is the factorial symbol

### The Perfect Cipher: The One-Time Pad
Essentially, a classical cipher can't be secure unless it comes with a huge key, but encrypting with a huge key is impractical. However, a OTP is such a cipher, and it is the most secure cipher. In fact, it guarantees perfect secrecy; even if the attack has unlimited computing power, it's impossible to learn anything about the plaintext except for its length. 

Encryption and Decryption - 
OTP takes a plaintext `P` and a random key `K` thats the same length as `P` and produces a ciphertext `C`. 

- `C = P ⊕ K`

Where C, P, and K are bit strings of the same length and ⊕ is the bitwise exclusive OR operation (XOR) defined as 0 ⊕ 0 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1, 1 ⊕ 1 = 0.

The OTP's decryption is identical to encryption; it's just an XOR: P = C ⊕ K. 



⊕⊕⊕⊕




