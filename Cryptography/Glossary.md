# DumLum's Cryptography Glossary

## Actuator
A device that receives an electronic signal from a controller and responds by interacting with its environment to produce an effect on some parameter of a physical, chemical or biological entity.

## Advanced Encryption Standard (AES)
Specifies a U.S government approved cryptographic algorithm that can be used to protect electronic data. The AES algo is a symmetric block cipher that can encrypt (exchipher) and decrypt (decipher) information. This standard specifies the Rijndael algorithm, a symmetric block cipher that can process blocks of 128 bits using cipher keys with lengths of 128, 192 and 256 bits.

## Application Proxy
A system that acts as a relay of application-level traffic

## Asymmetric Encryption
A form of crpyotsystem in which encryption and decryption qare performed using two diffeent keys, one of which is referred to as the public key and one of which is referred to as the private key. Also known as public-key encryption.

## Authentication
The process of verifying an identity claimed by or for a system entity.

## Authentication Exchange
An exchange of information between two parties over a network that verifies the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system.

## Authenticator 
Additional information appended to a message to enable the receiver to verify that the message should be accepted as authentic. The authenticator may be functionally independent of the content of the message itself (e.g a none or a source identifier) or it may be a function of the message contents (e.g a hash value or a cryptographic checksum)

## Authenticity
The property of being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or message originator

## Availability 
The property of a system or a system resource being accessible and usable upon demand by an authorized system entity, according to performance specifications for the system; i.e a system is available if it provides services according to the system design whenever users request them.

## Avalanche Effect
A characteristic of an encryption algorithm in which a small change in the plaintext or key gives rise to a large change in the ciphertext. For a hash code, the avalanche effect is a characteristic in which a small change in the message gives rise to a large change in the message digest.

## Backward Unpredictability
In a pseudorandom number stream, it is not feasible to determine the seed from knowledge of any generated values.

## Bacteria 
Program that consumes system resources by replicating itself

## Base64 transfer encoding
A binary-to-text encoding scheme that represent binary data in an ASCII string format by translating 6 bits of data into an 8-bit representation of a character

## Big Endian
A byte format in which the most significant byte of a word is in the low-address (leftmost) byte position.

## Bijection
A one-to-one correspondence

## Birthday Attack
This cryptanalytic attack attempts to find two values in the domain of a function that map to the same value in it's range.

## Block chaining
A procedure used during symmetric block encryption that makes an output block dependent not only on the current plaintext input block and key, but also on earlier input and/or output. The effect of block chaining is that two instances of the same plaintext input block will produce different ciphertext blocks, making cryptanalysis more difficult.

## Block Cipher
A symmetric encryption algorithm in which a block of plaintext bits (typically 64 or 128) is transformed as a whole into a ciphertext block of the same length

## Block cipher mode of operation
A technique for enhancing the effect of a cryptographic algorithm or adapting the algorithm for an application, such as applying a block cipher to a sequence of data blocks or a data stream.

## Byte
A sequence of 8 bits. Also referred to as an octet.

## Cipher
An algorithm for encryption and decryption. A cipher replaces a piece of information (an element in plaintext) with another object with the intent to conceal meaing. Typically, the replacement rule is governed by a secret key.

## Ciphertext
The output of an encryption algorithm; the encrypted form of a message or data.

## Ciphertext Stealing
A block cipher mode of operation technique in which the processing of the last block "steals" a temporary ciphertext of the penultimate block to complete the cipherblock.

## Circuit-level proxy
A system that acts as a relay between two TCP connections

## Code
An unvarying rule for replacing a piece of information (e.g letter, word, phrase) with another object, not necessarily of the same sort. Generally, there is no intent to conceal meaning. Examples include the ASCII character code (each character is represented by 7 bits) and frequency-shift keying (each binary value is represented by a particular frequency) 

## Commutative
A binary operation in which changing the order of the operands does not change the result.

## Composite Number
An integer that is not prime

## Compression Function
A function used repeatedly in a hash algorithm.

## Computationally Secure
Secure because the time and/pr cost of defeating the security are too high to be feasible.

## Confidentiality 
Preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information. A loss of confidentiality is the unauthorized disclosure on information.

## Confusion
A cyptographic technique that seeks to make the relationship between the statistics of the ciphertext and the value of the encryption key as complex as possible. This is achieved by the use of a complex scrambling algorithm that depends on the key and the input. 

## Constrained Device
A device with limited volatile and nonvolatile memory, limited processing power and a low data rate transceiver.

## Conventional Encryption
Symmetric Encryption

## Core
A network that connects geographically dispersed fog networks as well as providing access to other networks that are not part of the enterprise network.

## Covert Channel
A communications channel that enables the transfer of information in a way unintended by the designers of the communications facility.

## Cryptanalysis
The branch of cryptology dealing with the breaking of a cipher to recover information or forging encrypted information or forging encrypted information that will be accepted as authentic.

## Cryptographic Algorithm
An algorithm that uses the science of cryptography, including (a) encryption algorithms (b) cryptographic hash algorithms (c) digital signature algorithms and (d) key-agreement algorithms.

## Cryptographic Checksum
An authenticator that is a cryptographic function of both the data to be authenicated and a secret key. Also referred to as a message authentication code (MAC) 

## Cryptographic Hash Function
An algorithm for which it is computationally infeasible (because no aattack is significantly more efficient that brute force) to find either (a) a data oject that maps to a pre-specified hash result (the one-way property) or (b) two data objects that map to the same hash result (the collision-free property)

## Cryptography
The branch of cryptology dealing with the design of algoorithms for encryption and decryption, intended to ensure the secrecy and/or authenticity of messages.

## Cryptology
The study of secure communications, which encompasses both cryptogrpahy and cryptanalysis

## Cryptoperiod
Time span during which a specific cryptographic key is authorized for use for its defined purpose

## Cryptosystem (Cryptographic System)
A set of cryptographic algorithms together with the key management processes that support use of the algorithms in some application context.

## Data Origin Authentication
Provides for the corroboration of the source of a data unit. It does not provide protection against the duplication or modification of data units. This type of service supports applications like electronic mail, where there are no ongoing interactions between the communicating entities.

## Deciphering
Decryption

## Deeply Embedded System
A system that has a processor whose behaviour os difficult to observe both by the programmer and the user. A deeply embedded system uses a microcontroller, is not programmable once the program logic for the device has been burned into ROM (read-only memory), and has no interaction with a user.

## Deskewing Algorithm
A technique to add additional randomness to a random bit stream

## Detached Signature
A digital signature that may be stored and transmitted separately from the message it signs.

## Differential Cryptanalysis
A technique in which chosen plaintexts with particular XOR difference patterns are encrypted. The difference patterns of the resulting ciphertext provide information that can be used to determine the encryption key.

## Diffusion
A cryptographic technique that seeks to obscure the statistical structure of the plaintext by spreading out the influence of each individual plaintext digit over many ciphertext digits.

## Digital Signature Algorithm (DSA)
An authN mechanism that enables the creator of a message to attach a code that acts as a signature. The signature is formed by taking the hash of the message and encrypting the message with the creator's private key. The signature guarantees the source and integrity of the message.

## Digram
A two letter sequence. In English and other languages, the relative frequency of various digrams in plaintext can be used in the cryptanalysis of some ciphers. Also called digraph.

## Direct Digital Signature
Refers to a digital signature scheme that involves only the communicating parties (source, destination). It is assumed that the destination knows the public key of the source.

## Discrete Logorithm / Index
Basically a logarithm but in modular arithmetic. While regular logarithms are easy to compute, discrete logarithms are really hard to compute (when the numbers are huge).

## Discretionary Access Control
An access control service that enforces a security policy based on the identity of system entities and their authorizations to access system resources. This service is termed "discretionary" because an entity might have access rights that permit the entity, by its own volition, to enable another entity to access some resource. i.e the owner of a file/resource decides who can access it. Contrast: In mandatory access control, the system enforces strict rules that even owners can't override (like in military/government systems where clearance levels matter more than ownership).

## Divisor
One integeris said to be a devisor of another integer if there is no remainder on division.

## Edge
In the context of IoT, the network of IoT devices.

## ElGamal Digital Signature
A digital signature algorithm used by a number of applications

## Elliptic Curve
Defined by an equation between two variables with coefficients.

## Elliptic Curve Digital Signature Algorithm (ECDS) 
A public key-encryption algorithm based on elliptic curves.

## Elliptic Curve Cryptography
The use of cryptogrpahic algorithms based on elliptic curves

## Embedded System
Refers to the use of electronics and software within a product that has a specific function or set of functions, as opposed to a general-purpose computer, such as a laptop or desktop system. We can also define an embedded system as any device that includes a computer chip, but that is not a general purpose workstation, desktop or laptop computer.

## Enciphering
Encryption

## Encryption
The conversion of plaintext or data into unintelligible form by menas of a reversible translation, based on a translation table or algorithm. Also called enciphering

## End-to-end Encryption
Continuous protection of data that flows between two points in a network, effected by encrypting data whhen it leaves its source, keeping it encrypted while it passes through any intermediate computers (such as routers) and decrypting it only when it arrives at the intended final destination.

## Entropy Source
A source of random bits

## Error-correction Code
A code in which each charatcer or signal conforms to specific rules of construction so that deviations from these rules indicate the presence of an error and in which some or all of the detected errors can be corrected automatically.

## Federated Identity Management
A system that involves the use of a common identity management scheme acorss multiple enterprises and numerous applications and supporting many thousands, even millions of users.

## Feistel Cipher
A classic, and still common, structure for symmetric encryption.

## Field
A set of elements on which addition, subtraction, multiplication, and division are defined and behave as the corresponding operations on rational and real numbers do. A field is this a fundamental algebraic structure, which is widely used in algebra, number theory and many other areas of mathematics.

## Finite Field
A field with a finite number of elements.

## Fog
A collection of devices deployed physically near the edge of an IoT network; that is, near the sensors and other data-generating devices.Thus, some of the basic processing of large volumes of generated data is offloaded and outsourced from IoT software located at the centre.

## Forward Unpredictability
In a pseudorandom number stream, if the seed is unknown, the next output bit in the sequence should be unpredictable in spite of any knowledge of previous bits in the sequence.

## Greatest Common Divisor (GCD)
The GCD of two integers, a and b, is the largest positive integer that divides both a and b. One integer is said to divide another integer if there is no remainder on division.

## Group key
A key used by multiple entities

## Hash Code / Value
Output of a hash function

## Hash Function
A function that maps a variable-length data block or message into a fixed-length value called a hashcode. The function is designed in such a way that, when protected, it provides an authenticator to the data or message. Also referred to as a message digest.

## Identity Element
An element of a set with respect to a binary operation on that set, which leaves other elements unchanged whem combined with them

## IEEE 802.11
A standard for wireless local area networks.

## Initialization Vector
A random block of data that is used to begin encryption of multiple blocks of plaintext, when a block-chaining encryption technique is used. The IV serves to foil known-plaintext attacks.

## IP Security (IPsec)
A security enhancement to IPv4 and IPv6

## IPv4
The Internet Protocol (IP) version that was universally used until the advant of IPv6.

## IPv6
The Internet Protocol version intended to replace IPv4. It's most notable improvement over IPv4 is the use of longer address lengths.

## Irreversible Mapping
A transformation of data such that the original data cannot be recovered from the transformed data.

## Kerberos
The name given to Project Athena's code authentication service.

## Key Distribution
The distribution of encryption keys to two or more parties.

## Key Distribution Center
A system that is authorized to transmit temporary session keys to principals. Each session key is transmitted in encrypted form using a master key that the key distribution center shares with the target principal.

## Key Exchange
A procedure whereby two communicating parties can cooperate to acquire a shared cryptographic key.

## Key Expansion
The generation of subkeys from a key

## Key Management
A mechanism or set of mechanisms for managing the creation, storage, distribution and disposal of cryptographic keys.

## Key Wrapping
A method of securely exchanging a symmetric key to be shared by two parties, using a symmetic key already shared by those parties.

## Keyless Algorithm 
A cryptographic algorithm, such as a hash algorithm, that does not use a key.

## Keystream
A stream of bits used as the key for a stream encryption algorithm

## Lightweight Cryptographic Algorithm
A cryptographic algorithm designed for resource-constrained devices

## Lightweight Cryptography
A subfield of cryptography concerned with the development of cryptoanalytic algorithms for resource-constrained devices.

## Little Endian
A byte format in which the least significant byte of a word is in the low-address (leftmost) byte position

## Logic Bomb
Logic embedded in a computer program that checks for a certain set of conditions to be present on the system. When these conditions are met, it executes some function resulting in unauthorized actions.

## Mandatory Access Control
A means of restricting access to objects based on fixed security attributes assigned to users and to files and other objects. The controls are mandatory in the sense that they cannot be modified by users or their programs. See also Discretionary Access Control to see the contrast.

## Master Key
A longer lasting key that is used between a key distribution center and a principal for the purpose of encoding the transmission of session keys. Typically, the master keys are distributed by noncryptographic means. Also reffered to as a key-encrypting key.

## Media Access Control
For broadcast networks, the method of determining which devices has access to the transmission medium at any time. 

## Meet-in-the-middle attack
This is a cryptanalytic attack that attempts to find a value in each of the range and domain of the composition of two functions such that the forward mapping of one through the first function is the same as the inverse image of the other through the second function - quite literally meeting in the middle of the composed function. 

## Message Authentication
A process used to verify the integrity of a message.

## Message Authentication Code (MAC)
Cryptographic checksum

## Microcontroller
A single chip that contains the processor, non-volatile memory for the program (ROM or flash), volatile memory for input and output (RAM), a clock, and an I/O control unit.

## Modular Arithmetic
A kind of integer arithmetic that reduces all numbers to one of a fixed set [0, ..., n - 1] for some number n. Any integer outside this range is reduced to one in this range by taking the remainder after division by n

## Mode of Operation
A technique for enhancing the effect of a cryptographic algorithm or adapting the algorithm for an application, such as applying a block cipher to a sequence of data blocks or a data stream.

## Modulus
If a is an interger and n is a positive integer, we define a mod n to be the remainder when a is divided by n. The integer n is called the modulus. 

## Monoalphabetic Substitution Cipher
A single cipher alphabet (mapping from plain alphabet to cipher alphabet) is used per message. 

## Multiple Encryption
Repeated use of an encryption function with different keys to produce a more complex mapping from plaintext to ciphertext.

## Nibble
A sequence of 4 bits.

## Non-repudiation
Assurance that the sender of information is provided with proof of delivery and the recipient is provided with proof of the sender's identity, so neither can later deny having processed the information.

## Nonce
An identifier or number that is used only once.

## Notarization
The use of a trusted third party to assure certain properties of a data exchange

## One-time pad (OTP)
An encryption scheme in which the key length is equal to the message length, with each element (bit or character) of the key used to encrypt/decrypt each element of the message (e.g by XOR). The key is randomly chosen and used only once, for a single message. If the key is secure, this scheme is impossible to break.

## One-way function
A functino that is easily computed, but the calculation of it's inverse is infeasible (e.g hash)

## OSI Security Architecture
A management-oriented security standard that focuses on the OSI model and on networking and communications aspects of security.

## Pairwise Keys
Cryptographic keys used for communication between a pair of devices, typically between an STA and an AP. These keys form a hierarchy beginning with a master key from which other keys are derived dynamically and used for a limited period of time. 

## Peer Entity Authentication
Provides for the corroboration of the identity of a peer entity in an association. Two entities are considered peers if they implement the same protocol in different systems; e.g two TCP modules in two communicating systems.

## Permutation
An ordered sequence of all the elements of a finite set of elements S, with each element appearing exactly once.

## Plaintext
The input to an encryption function or the output of a decryption function.

## Polyalphabetic Substitution Cipher
The use of different monoalpabetic substitutions as one proceeds through the plaintext message. 

## Post-quantum Cryptography Algorithm
A cryptographic algorithm designed using the principles of post-quantum cryptography.

## Post Office Protocol (POP3)
An email protocol

## Prime Number
An integer p > 1 is a prime number if and only if it's only divisors are +-1 and +-itself

## Primitive Root
A primitive root modulo n is a number that, when you keep multiplying it by itself and take remainders, cycles through all possible non-zero remainders that don't share factors with n.

## Private Key
One of the two keys used in an asymmetric encryption system. For secure communication, the private key should only be known to its creator

## Product Cipher
The execution of two or more simple ciphers in sequence in such a way that the final result or product is cryptographically stronger than any of the component ciphers.

## Pseudorandom function (PRF)
A function that produces a pseudorandom string of bits of some fixed length

## Pseudorandom Number Generator
A function the deterministically produces a sequence of numbers that are apparently statistically random

## Public Key
One of the two keys used in an aymmetric encryption system. The public key is made public and is to be used in conjuntion with a corresponding private key.

## Public-key Certificate
Consists of a public key plus a User ID of the key owners with the whole block signed by a trusted third party. Typically, the third party is a certificate authority (CA) that is trusted by the user community, usch as a governmnet agency or a financialinstitution. 

## Public-Key Infrastructure
Asymmetric encryption

## Public-Key Infrastructure (PKI)
The set of hardware, software, people, policies, and procedures needed to create, manage, store, distribute, and revoke digital certificates based on asymmetric cryptography.

## Quantum Computing
A form of computing is based on the representation of information in a form analogous to the behaviour of elementary particles in quantum physics

## Quantum Safety
Refers to cryptographic algorithms that are safe, or secure, against quantum computing algorithms.

## Relatively Prime
Two numbers are relatively prime if they have no prime factors in common; that is, their only common divisor is 1

## Residue
When the integer a is divided by the integer n, the remainder r is referred to as the residue. Equivalently, r = a mod n

## Residue Class
All the integers that have the same remainder when divided by n form a residue class (mod n). Thus, for a given remainder r, the residue class (mod n) to which it belongs consists of the integers r, r += n, r +- 2n ..

## Reversible Mapping
A transformation of data such that the original data can be recovered from the transformed data.

## Round
A sub-algorithm in a cryptographic algorithm that is repeated multiple times.

## Round function
The functoin performed by a round

## Routing Control
Enables selection of particular physically or logically secure routes for certain data and allows routing changes, espeically when a breacj pf security is suspected.

## RSA Algorithm
A public-key encryption algorithm based on exponentiation in modular-arithmetic. It is the only algorithm generally accepted as practical and secure for public-key encryption.

## S-Box
A matrix structure that is used as part of some block cipher algorithms to perform substitution

## Secret Key
The key used in a symmetric encryption system. Both participants must share the same key, and this key must remain secret to protect the communication.

## Seed
The inout to a pseudorandom number generator

## Session Key
A temporary encryption key used between two principals

## Single-key algorithm
Encryption that uses a single secret key

## Skew
Bias in a random or pseudorandom bit stream

## Steganography
Methods of hisding the existence of a message or other data. This is different than cryptography, which hides the meaning of a message but does not hide the message itself

## Stream Cipher
A symmetric encryption algorithm in which ciphertext output is produced bit-by-bit or byte-by-byte from a stream of plaintext input

## Subkey
A key derived from the main key of an ecryption algorithm, generally used for only one round.

## Substitution
A basic mechanism of encryption in which one bit or block of data is substituted for another

## Symmetric Encryption
A form of cryptosystem in which encryption and decryption are performed using the same key. Also known as conventional encryption

## System Integrity
Assures that a system performs its intended function in an unimpaired manner, free from deliberate or inadvertant unauthorized manipulation of the system

## Timing Attack
An attack that depends on the running time of the decryption algorithm

## Transceiver 
A device that contains the electronics needed to transmit and receive data. Most IoT devices contain a wireless transceiver, capable of communication using WiFI, etc

## Transport Mode
A mode of operation of IPSec that provides protection to the payload of an IP packet.

## Trapdoor
Secret undocumented entry point into a program used to grant access without normal methods of access authentication

## Trapdoor one-way function
A function that is easily computed, and the calculation of its inverse is infeasible unless certain privileged information is known.

## Triple DES (3DES)
Multiple encryption using three instances of DES, with either 2 or 3 different keys

## True Random Generator
Produces bits non-deterministically using some physical source that has produces some sort of random output

## Tunnel Mode
A mode of operation of IPSec that provides protection to both the payload and header of an IP packet

## Tweakable Block Cipher
A cipher that has 3 inputs: a plaintext p, a symmetric key K, and a tweak T; and produces a ciphertext output C.

## Two-key Algorithm
A cryptographic algorithm that uses apublic and a private key.

## Unconditionally Secure
Secure even against an opponent with unlimited time and unlimited computing resources

## Unpredictability
The property of a stream of bits that future bits are not predictable from preceding bits.

## Zombie
A program that secretly takes over another internet-attached computer and then uses that computer to launch attacks that are difficult to trace to the zombie's creator.
