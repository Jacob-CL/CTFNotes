# Chapter 1: Information and Network Security Concepts
Learning Objectives
- Describe the key security requirements of confidentiality, integrity, and availability.
- Discuss the types of security threats and attacks that must be dealt with and give examples of the types of threats and attacks that apply to different categories of
computer and network assets.
- Provide an overview of keyless, single-key, and two-key cryptographic algorithms.
- Provide an overview of the main areas of network security.
- Describe a trust model for information security.
- List and briefly describe key organizations involved in cryptography standards.

## 1.1 CyberSecurity, Information Security and Network Security
As subsets of Cybersecurity we can define the following:
- `Information Security`: security: This term refers to preservation of confidentiality, integrity, and availability of information. In addition, other properties, such as authenticity, accountability, nonrepudiation, and reliability can also be involved.
- `Network Security`: This term refers to protection of networks and their service from unauthorized modification, destruction, or disclosure, and provision of assurance that the network performs its critical functions correctly and there are no harmful side effects.

Security Objectives (CIA Triad)
- `Confidentiality` covers data confidentiality and privacy
- `Integrity` covers data and system integrity
- `Availability`

Some argue the need for more than just those 3:
- `Accountability`: The security goal that generates the requirement for actions of an entity to be traced uniquely to that entity.
- `Authenticity`: The property of being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or message originator.

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
