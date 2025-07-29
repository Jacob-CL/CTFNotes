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
- `Security Service`: A processing or comm service that enahces the security of the data processing systems and the information transfer of an organization. The services are intended to count security attacks, and they make use of one or more security mechanisms to provide the service .

The terms `threat` and `attack` are commonly used, with the following meanings:
- `Threat`: Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image, or reputation), organizational assets, individuals, other organizations, or the Nation through an information system via unauthorized access, destruction, disclosure, modification of information, and/or denial of service.
- `Attack`: Any kind of malicious activity that attempts to collect, disrupt, deny, degrade or destroy information system resources or the information itself.

## 1.3 Security Attacks
A means of classifying security attacks - `passive` or `active`
- `Passive`: These include eavesdropping type attacks like traffic analysis or the release of message contents. Passive attacks are very difficult to detect because they do not involve any alteration of data and once a packet leaves our network, it's impossible to really know what happens to it like a third-party listening to it. This type of attacks is countered with strong encryption.
- `Active`: These involve some kind of modification of the data stream or the creation of a flase stream and can be subdivided in 4 categories: `replay`, `masquerade`, `modification of message` and `denial of service`. These are much easier to detect if you have the tools and logic set up to do so.
  - Masquerade takes place when one entity pretends to be another. (MiTM)
  - Replay involves the passive capture of a data unit and its subsequent retransmission to produce an unauthorized effect.
  - DoS prevents or inhibits normal use or management of communication facilities. (Flooding the server with an overwhelming amount of data AND/OR triggering some action the server that consume substantial computing resources.
 
## 1.4 Security Services
















