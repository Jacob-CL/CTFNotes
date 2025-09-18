# Chapter 3 - Classical Encryption Techniques
Symmetric encryption, also referred to as conventional encryption or single-key encryption, was the only type of encryption in use prior to the development of public-key encryption in the the 1970s. It reamins the most widely used.

## 3.1 Symmetric Cipher Model
A symmetric encryption scheme has 5 ingredients:
1. Plaintext: This is the original intelligible message or data that is fed into the algorithm
2. Encryption algorithm: The encryption algorithm performs various substitutions and tranformations on the plaintext.
3. Secret key: The secret key is also input to the encryption algo. The key is a value indepedent of the plaintext and of the algo. The algo will produce a different output depending on the specific key being used at the time. The exact substitutions and transformations performed by the algo depend on the key.
4. Ciphertext: This is the scrambled message produced as output. It depedns on the plaintext and the secrey keys. For a given message, 2 different keys will produce two different ciphertexts. The ciphertext is an apparently random stream of data, as it stands is unintelligibile.
5. Decrpytion algorithm: This is essentially the encryption algo run in reverse. It takes the ciphertext and the secret and produces the original plaintext.

To use such a methodology securely, you need to have a strong encryption algo and the sender and receiver must have obtained copies of the secret key in a secure fashion, and obviously kept secure as well.

### Cryptology
Cryptographic systems are characterized along 3 indepedent dimensions
1. Type of operations used for transforming plaintext to ciphertext
2. The number of keys used
3. The way in which the plaintext is processed
