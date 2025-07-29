# Chapter 1: Information and Network Security Concepts
## 1.1 CyberSecurity, Information Security and Network Security
As subsets of Cybersecurity we can define the following:
- `Information Security`: Preservation of confidentiality, integrity, and availability of information. In addition, other properties, such as authenticity, accountability, nonrepudiation, and reliability can also be involved.
- `Network Security`: Protection of networks and their service from unauthorized modification, destruction, or disclosure, and provision of assurance that the network performs its critical functions correctly and there are no harmful side effects.

Security Objectives (CIA Triad)
- `Confidentiality` covers data confidentiality and privacy
- `Integrity` covers data and system integrity
- `Availability`

Some argue the need for more than just those 3:
- `Accountability`: Events and actions can be traced uniquely to that entity.
- `Authenticity`: Being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or message originator.

Challenges of Information Security:
1. Although we may be able to simplify InfoSec into the CIA, or CIAAA - the mechanisms used to meet those requirements can be very complex.
2. Most successful attacks come from left-of-field thinking, or 'unforeseen creativity'.
3. Because of point 2, the procedures used to provide particular services are often counterintuitive. It's not always obvious why it's so complicated but sometimes considering the threats to that particular mechanism might shed light on why it's so elaborate
4. Security Mechanisms typically involve more than a particular algorithm or protocol - they also require that participants be in possession of some secret information, or a reliance on some other communication protocol who bahviour may complicate things
5. CyberSecurity are esentially a battle of wits between perpetrator who tries to find holes and the designer of administrator who tries to close them. The attacker has the advantage that they only need to find a single weakness where the designer must and find and elimate them all.
6. There is ittle natural tendency on the part of the users and system managers to perceive little benefit from security investment until a security failure occurs.
7. Security requires regular, even constant, monitoring and this is difficult in todays short-term, overloaded environment.
8. Security is mostly an afterthought to be incorporated after the design
9. Many users perceive strong security as an impediment to efficient and user-friendly operation of an info system or use of information

## 1.2 The OSI Security Architecture
The open systems interconnection (OSI) security architecture is useful to managers as a way of organizing the task of providing security. It focuses on:
- `Security Attacks`: Any action that compromises the security of information owned by an org
- `Security Mechenism`: A process (or a device incorporating such a process) that is designed to detect, prevent, or recover from a security attack.
- `Security Service`: A processing or comm service that enahces the security of the data processing systems and the information transfer of an organization. The services are intended to count security attacks, and they make use of one or more security mechanisms to provide the service.

X.800 is an ITU-T recommendation that defines a security architecture for Open Systems Interconnection (OSI). It provides a framework for understanding and implementing security services and mechanisms within the OSI mode

The terms `threat` and `attack` are commonly used, with the following meanings:
- `Threat`: Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, or the Nation through an information system via unauthorized access, destruction, disclosure, modification of information, and/or denial of service.
- `Attack`: Any kind of malicious activity that attempts to collect, disrupt, deny, degrade or destroy information system resources or the information itself.

## 1.3 Security Attacks
A means of classifying security attacks - `passive` or `active`
- `Passive`: These include eavesdropping type attacks like traffic analysis or the release of message contents. Passive attacks are very difficult to detect because they do not involve any alteration of data and once a packet leaves our network, it's impossible to really know what happens to it like a third-party listening to it. This type of attacks is countered with strong encryption.
- `Active`: These involve some kind of modification of the data stream or the creation of a flase stream and can be subdivided in 4 categories: `replay`, `masquerade`, `modification of message` and `denial of service`. These are much easier to detect if you have the tools and logic set up to do so.
  - `Masquerade` takes place when one entity pretends to be another. (MiTM)
  - `Replay` involves the passive capture of a data unit and its subsequent retransmission to produce an unauthorized effect.
  - `DoS` prevents or inhibits normal use or management of communication facilities. (Flooding the server with an overwhelming amount of data AND/OR triggering some action the server that consume substantial computing resources.
 
## 1.4 Security Services
A security serivice is a capability that supports one or more of the security requirements (CIAAA). Security Services implement security policies and are implemented by security mechanisms. 
- `Authentication` service is conncerned with assuring that a communication is authentic. Two AuthN services are defined in X.800:
  - `Peer Entity AuthN`: Provides for the corroboration of the identity of a peer entity in an association. Two entities are considered peers if they implement the same protocol in different systems; for example, two TCP modules in two communicating systems. (This is like verifying the identity of someone you're having a conversation with right now)
  - `Data Origin AuthN`: Provides for the corroboration of the source of a data unit. It does not provide protection against the duplication or modification of data units. This type of service supports applications like electronic mail, where there are no ongoing interactions between the communicating entities. (This is like checking the return address on a letter to make sure it really came from who it says it did)

The key difference: the first is about ongoing conversations, the second is about one-way messages.

- `Access Control`: is the ability to limit and control the access to host systems and applications via communication links. Acheiving this means each entity trying to gain access must first me identified, or authenticated, so that access rights can be tailored to the individual. e.g Password systems, keycards, VPNs, file permissions, Azure RBAC.
- `Data Confidentiality`: The protection of transmitted data from passive attacks (traffic analysis and/or content release). e.g HTTPS, VPNs (again), Encrypted harddrives
- `Data Integrity`: As with above, iintegrity can apply to a stream of messages, a single message or selected fields within a message. But also like before, the most useful and straightforward approach is total stream protection. This includes messages are received as sent with no duplication, insertion, modification, reordering or replays and of course destruction. Now if it were a connectionless integrity service, one that deals with individual messages (like data origin authN) without the regard to any larger contexct, generally provides protection against message modification only. And since integrity services relate to active attacks, we are concerned with detection rather than prevention. e.g Digital signatures on software, checksums, banking transactions where they've checked if amounts of changed in transit, email signing.
- `Nonrepudiation`: prevents either sender or receiver from denying a transmitted message. Thus when a message is sent, the receiver can prove that the alleged sender in fact sent the message. Similarly, when a message is received, the sender can prove that the alleged receiver in fact recieved the message. e.g Digital signatures on contracts, email read receipts, certified mail, blockchain transactions.
- `Availability Service`: is simply a property of a system, or a sysdtem resource being accessible and usable upon demand by an authZ system entity. An availability service is one that protects a system to ensure its availability. This service addresses the security concerns raised by DoS attacks. e.g Content Delivery Networks (CDNs), DDos protection services (cloudflare), backup power services, load balancers.

## 1.5 Security mechanisms
- `Cryptographic algorithms`: We can distinguish between reversible cryptographic mechanisms and irreversible cryptographic mechanisms. A reversible cryptographic mechanism is simply an encryption algorithm that allows data to be encrypted and subsequently decrypted. Irreversible cryptographic mechanisms include hash algorithms and message authentication codes, which are used in digital signature and message authentication applications.
- `Data integrity`: This category covers a variety of mechanisms used to assure the integrity of a data unit or stream of data units.
- `Digital signature`: Data appended to, or a cryptographic transformation of, a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery.
- `Authentication` exchange: A mechanism intended to ensure the identity of an entity by means of information exchange.
- `Traffic padding`: The insertion of bits into gaps in a data stream to frustrate traffic analysis attempts.
- `Routing control`: Enables selection of particular physically or logically secure routes for certain data and allows routing changes, especially when a breach of security is suspected.
- `Notarization`: The use of a trusted third party to assure certain properties of a data exchange.
- `Access control`: A variety of mechanisms that enforce access rights to resources.

## 1.6 Cryptography
Cryptography is a branch of mathematics that deals with the transformation of data - it's an essential component in the secure storage and tramission of data, and in the secure interaction between parties. Algos can be divided into 3 categories:
- `Keyless` (Hash functions): Do not use any keys during cryptographic transformations. They are deterministic functions that have certain properties useful for cryptography. `Hashes` are keyless algorithms as a hash function turns a variable amount of text into a small fixed-length value called a `hash value`, `hash code` or `digest`. A cryptographic hash function is one that has additional properties that make it useful as part of another cryptographic algorithm, such as a message authentication code or a digital signature.
- `Single-key` (Symmetric Encryption): Single-key cryptographic algorithms depend on the use of a secret key. This key may be known to a single user; for example, this is the case for protecting stored data that is only going to be accessed by the data creator. Commonly, two parties share the secret key so that communication between the two parties is protected. Encryption algorithms that use a single key are referred to as symmetric encryption algorithms. They come in 2 forms:
  - `Block Cipher`: A block cipher operates on data as a sequence of blocks. A typical block size is 128 bits. In most versions of the block cipher, known as modes of operation, the transformation depends not only on the current data block and the secret key but also on the content of preceding blocks.
  - `Stream Cipher`: A stream cipher operates on data as a sequence of bits. Typically, an exclusive-OR operation is used to produce a bit-by-bit transformation. As with the block cipher, the transformation depends on a secret key.

Another form of single-key cryptographic algorithm is the `message authentication code` (MAC). A `MAC` is a data element
associated with a data block or message. The MAC is generated by a cryptographic transformation involving a secret key and,
typically, a cryptographic hash function of the message. The MAC is designed so that someone in possession of the secret key can verify the integrity of the message. Thus, the MAC algorithm takes as input a message and secret key and produces the MAC.

- `Two-key` (Asymmetric encryption): At various stages of the calculation, two different but related keys are used, referred to as a private key and a public key. A private key is known only to a single user or entity, whereas the corresponding public key is made available to a number of users. Can work in two ways:
1. Sign with Private, Verify with Public. You lock/encrypt something with your private key --> Anyone can unlock/decrypt it with your public key --> Purpose: This proves YOU sent it (like a signature)
2. Encrypt with Public, Decrypt with Private. Anyone can lock/encrypt something with your public key --> Only YOU can unlock/decrypt it with your private key (not even the original sender) --> Purpose: This keeps messages secret and meant only for you

Asymmetric encryption is really useful for:
- `Digital signatures`: You "sign" a document using your private key --> Anyone can check your signature using your public key --> This proves two things: who sent it and that it wasn't changed. e.g When you get a software update, it's digitally signed so you know it's really from Apple/Microsoft and hasn't been infected with malware.
-  `Key Exchange`: You use asymmetric encryption to safely pass that secret code --> Once you both have the secret code, you switch to using it (because it's much faster than asymmetric encryption) e.g When you visit a website with HTTPS, your browser and the server use this method to agree on a shared secret for that session
-  `User Authentication`: You prove your identity without giving away your password --> The system verifies you're genuine, and you verify the system is genuine too. e.g Using a security key like a YubiKey to log into something - it uses asymmetric encryption to prove you're really you.

Ultimately - Asymmetric encryption is mainly used for proving identity, ensuring nothing was tampered with, and safely sharing secrets.

## 1.7 Network Security

## 1.8 Trust and Trustworthiness

## 1.9 Standards

## 1.10 Key terms, review questions and problems
1.1 What is the OSI security architecture?

1.2 What is application security in networking?

1.3 List the differences between adware and ransom ware.

1.4 What is the most effective measure to take against a cross-site request forgery?

1.5 List and briefly define categories of security mechanisms.

1.6 List and briefly define the fundamental security design principles.

1.7 Provide an overview of the three types of cryptographic algorithms.

1.8 Which is worse in terms of firewall detection, a false positive or false negative and why?

1.9 Why are internal threats usually more effective than external threats?

1.10 What are the few major applications of cryptography in the modern world?

1.11 List the differences between hashing and encryption.

1.12 What do you know about cryptosystems? What is its significance?

1.13 Name the properties of interactive proof that are useful in cryptography.

Problems:
1.1 Consider an automated cash deposit machine in which users provide a card or an account number to deposit cash. Give examples of confiden tiality, integrity, and availability requirements associated with the system, and, in each case, indicate the degree of importance of the requirement.

1.2 Repeat Problem 1.1 for a payment gateway system where a user pays for an item using their account via the payment gateway.

1.3 Consider a financial report publishing system used to produce reports for various organizations.
  a. Give an example of a type of publication for which confidentiality of the stored data is the most important
requirement.
  b. Give an example of a type of publication in which data itegrity is the most important requirement.
  c. Give an example in which system availability is the most important requirement.

1.4 For each of the following assets, assign a low, moderate, or high impact level for the loss of confidentiality, availability, and integrity, respectively. Justify your answers.
  a. A student maintaining a blog to post public information.
  b. An examination section of a university that is managing sensitive information about exam papers.
  c. An information system in a pathological laboratory maintaining the patient's data.
  d. A student information system used for maintaining student data in a university that contains both personal,
academic information and routine administrative information (not privacy related). Assess the impact for the two data sets separately and the information system as a whole.
  e. A university library contains a library management system, which controls the distribution of books among the students of various departments. The library management system contains both the student data and the book data. Assess the impact for the two data sets separately and the information system as a whole.
  
1.5 If you work with a Linux server, what are the three significant steps you must take in order to secure it?













