# Wi-fi basics
- `WEP` (Wired Equivalent Privacy): The original WiFi security protocol, WEP, provides basic encryption but is now considered outdated and insecure due to vulnerabilities that make it easy to breach.
- `WPA` (WiFi Protected Access): Introduced as an interim improvement over WEP, WPA offers better encryption through TKIP (Temporal Key Integrity Protocol), but it is still less secure than newer standards.
- `WPA2` (WiFi Protected Access II): A significant advancement over WPA, WPA2 uses AES (Advanced Encryption Standard) for robust security. It has been the standard for many years, providing strong protection for most networks.
- `WPA3` (WiFi Protected Access III): The latest standard, WPA3, enhances security with features like individualized data encryption and more robust password-based authentication, making it the most secure option currently available.

<img width="1440" height="1286" alt="image" src="https://github.com/user-attachments/assets/3ff41cd6-0a90-440d-becc-07a898e5e94c" />

When it comes to wifi pentesting you're
- Evaluating passphrases + configuration
- Testing infrstructure + clients

## IEEE 802.11 Frame Types
- `Management (00)`: These frames are used for management and control, and allowing the access point and client to control the active connection. These are the ones we focus on in pentesting wifi as these frames are used to control the connection between the access point and the client. To filter them in WireShark, we would specify type `00` and subtypes like the following:
  - `Beacon Frames (1000)`: Beacon frames are primarily used by the access point to communicate its presence to the client or station. It includes information such as supported ciphers, authentication types, its SSID, and supported data rates among others.
  - `Probe Request (0100)` and `Probe Response (0101)`: The probe request and response process exist to allow the client to discover nearby access points. Simply put, if a network is hidden or not hidden, a client will send a probe request with the SSID of the access point. The access point will then respond with information about itself for the client.
  - `Authentication Request` and `Response (1011)`: Authentication requests are sent by the client to the access point to begin the connection process. These frames are primarily used to identify the client to the access point.
  - `Association/Reassociation Request and Responses (0000, 0001, 0010, 0011)`: After sending an authentication request and undergoing the authentication process, the client sends an association request to the access point. The access point then responds with an association response to indicate whether the client is able to associate with it or not.
  - `Disassociation/Deauthentication (1010, 1100)`: Disassociation and Deauthentication frames are sent from the access point to the client. Similar to their inverse frames (association and authentication), they are designed to terminate the connection between the access point and the client. These frames additionally contain what is known as a reason code. This reason code indicates why the client is being disconnected from the access point. We utilize crafting these frames for many handshake captures and denial of service based attacks during wi-fi penetration testing efforts.
- `Control (01)`: Control frames are used for managing the transmission and reception of data frames within wi-fi networks. We can consider them like a sense of quality control.
- `Data (10)`: Data frames are used to contain data for transmission.

## The Connection Cycle
This is the typical connection process between clients and access points and their WireShark filters:
1. `Beacon Frames` = Beacon frames are primarily used by the access point to communicate its presence to the client or station. It includes information such as supported ciphers, authentication types, its SSID, and supported data rates among others: `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 8)`
2. `Probe Request and Response` = The probe request and response process exist to allow the client to discover nearby access points. Simply put, if a network is hidden or not hidden, a client will send a probe request with the SSID of the access point. The access point will then respond with information about itself for the client: `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 4)` | `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 5)`
3. `Authentication Request and Response` = Authentication requests are sent by the client to the access point to begin the connection process. These frames are primarily used to identify the client to the access point: `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 11)` | `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 0)`
4. `Association Request and Response` = After sending an authentication request and undergoing the authentication process, the client sends an association request to the access point. The access point then responds with an association response to indicate whether the client is able to associate with it or not: `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 1)`
5. Some form of handshake or other security mechanism: `eapol`
6. `Disassociation/Deauthentication` = Disassociation and Deauthentication frames are sent from the access point to the client. Similar to their inverse frames (association and authentication), they are designed to terminate the connection between the access point and the client. These frames additionally contain what is known as a reason code. This reason code indicates why the client is being disconnected from the access point. We utilize crafting these frames for many handshake captures and denial of service based attacks during wi-fi penetration testing efforts: `(wlan.fc.type == 0) && (wlan.fc.type_subtype == 12) or (wlan.fc.type_subtype == 10)`

## Authentication Methods
<img width="1440" height="896" alt="image" src="https://github.com/user-attachments/assets/d4be27f5-614c-450a-966e-0b152f3b8df3" />

Shared Key Authentication:
<img width="1440" height="536" alt="image" src="https://github.com/user-attachments/assets/f7d05558-a538-4d05-94c5-ed5c63a3c47d" />

WPA uses a form of authN that includes a 4-way handshake, usually replacing the association process with more verbose verification but at a high level:
1. `Authentication Request`: The client sends an authentication request to the AP to initiate the authentication process.
2. `Authentication Response`: The AP responds with an authentication response, which indicates that it is ready to proceed with authentication.
3. `Pairwise Key Generation`: The client and the AP then calculate the PMK from the PSK (password).
4. `Four-Way Handshake`: The client and access point then undergo each step of the four way handshake, which involves nonce exchange, derivation, among other actions to verify that the client and AP truly know the PSK

## Wi-fi Interfaces
Computers transit and receive data through these interfaces. [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Cards%20and%20Chipsets) offers a comprehensive list of Wi-Fi adapters based on their performance.
- Check strength with `iwconfig` --> see `Tx-Power`. We can change the country with something like `sudo iw reg set US` to utilize a greater power but it may be illegal. The interface will automatically set its power to the maximum in our region but check in case.

You can manually change the `txpower`:
- Bring the interface down: `sudo ifconfig wlan0 down`
- Set `txpower`: `sudo iwconfig wlan0 txpower 30`
- Bring it back: `sudo ifconfig wlan0 up`
- FInally check to see it yourself: `iwconfig`

To see what the interface is capable of run: `iw list`
Scan available Wifi networks: `iwlist wlan0 scan | grep 'Cell\|Quality\|ESSID\|IEEE'`

## Configure Channels
See all available channels for the wireless interface: `iwlist wlan0 channel`
To then change to a particular channel, first disable: `sudo ifconfig wlan0 down` then `sudo iwconfig wlan0 channel 64` then `sudo ifconfig wlan0 up`, check with `iwlist wlan0 channel`
If we prefer to change the frequency directly rather than adjusting the channel, we have the option to do so as well: 
- Check with `iwlist wlan0 frequency | grep Current`
- Then `sudo ifconfig wlan0 down`
- `sudo iwconfig wlan0 freq "5.52G"`
- `sudo ifconfig wlan0 up`
- `iwlist wlan0 frequency | grep Current`

## Interface Nodes
`Managed Mode`: Managed mode is when we want our interface to act as a client or a station - this is normal / standard. To change it to Managed Mode:
- `sudo ifconfig wlan0 down` | ` sudo iwconfig wlan0 mode managed` | `sudo ifconfig wlan0 up`
- Then to connect to a network: `sudo iwconfig wlan0 essid WIFINAME`
- Always can see the setting enabled with `sudo iwconfig`

`Ad-hoc Mode`:  Essentially this mode is peer to peer and allows wireless interfaces to communicate directly to one another. This mode is commonly found in most residential mesh systems for their backhaul bands.
- `sudo iwconfig wlan0 mode ad-hoc` | Connect with: `sudo iwconfig wlan0 essid HTB-Mesh` | `sudo iwconfig`

`Master Mode`: The opposite to Managed Mode, but we can't set this with any command. It's enabled with some management daemon file.

`Mesh mode`: We can set our interface to join a self-configuring and routing network. This mode is commonly used for business applications where there is a need for large coverage across a physical space.
- `sudo iw dev wlan0 set type mesh`

`Monitor Mode`: In this mode, the network interface can capture all wireless traffic within its range, regardless of the intended recipient. Unlike normal operation, where the interface only captures packets addressed to it or broadcasted, monitor mode enables comprehensive network monitoring and analysis.
- `iwconfig` | `sudo ifconfig wlan0 down` | `sudo iw wlan0 set monitor control` | `sudo ifconfig wlan0 up` | `iwconfig`

## Intro to [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)
Is a suite of tools (20) designed for Wifi Network Security - Monitoring, Attacking, Testing, Cracking. The most common/useful are:
- `Airmon-ng`: can enable and disable monitor mode on wireless interfaces. It may also be used to kill network managers, or go back from monitor mode to managed mode.
- `Airodump-ng`: Can capture raw 802.11 frames.
- `Airgraph-ng`: Can be used to create graphs of wireless networks using the CSV files generated by Airodump-ng.
- `Aireplay-ng`: Can generate wireless traffic.
- `Airdecap-ng`: can decrypt WEP, WPA PSK, or WPA2 PSK capture files.
- `Aircrack-ng`: Can crack WEP and WPA/WPA2 networks that use pre-shared keys or PMKID.

Airmon-ng Commands
- Show Wireless Interface name, driver and chipset: `sudo airmon-ng`
- Start `wlan0` interface in monitor mode: `airmon-ng start wlan0` | Test with `iwconfig`
- Checking for interfering processes: `sudo airmon-ng check`. If there are issues in the pentest, then it's worth killing these processes just to be safe: `sudo airmon-ng check kill`
- Start monitor mode on a specific channel: `sudo airmon-ng start wlan0 11`
- Stop monitor mode: ` sudo airmon-ng stop wlan0mon`
- Always remember `iwconfig` for checking in on the interface

## Airodump-ng
Will dump a whole bunch of useful information including:

| **Field**   | **Description**                                                                 |
|-------------|---------------------------------------------------------------------------------|
| BSSID       | Shows the MAC address of the access points                                     |
| PWR         | Shows the "power" of the network. The higher the number, the better the signal |
| Beacons     | Shows the number of announcement packets sent by the network                   |
| #Data       | Shows the number of captured data packets                                      |
| #/s         | Shows the number of data packets captured in the past ten seconds              |
| CH          | Shows the "Channel" the network runs on                                        |
| MB          | Shows the maximum speed supported by the network                               |
| ENC         | Shows the encryption method used by the network                                |
| CIPHER      | Shows the cipher used by the network                                            |
| AUTH        | Shows the authentication used by the network                                   |
| ESSID       | Shows the name of the network                                                   |
| STATION     | Shows the MAC address of the client connected to the network                   |
| RATE        | Shows the data transfer rate between the client and the access point           |
| LOST        | Shows the number of data packets lost                                          |
| Packets     | Shows the number of data packets sent by the client                            |
| Notes       | Shows additional information about the client, such as captured EAPOL or PMKID |
| PROBES      | Shows the list of networks the client is probing for                           |

Airodump-ng Commands
- First the interface needs to be in monitor mode: `sudo airmon-ng start wlan0` | `iwconfig`
- Run airodump-ng: `sudo airodump-ng wlan0mon`
- Run on a specific channel: `sudo airodump-ng -c 11 wlan0mon`
- Scan 5ghz Wifi bands: ` sudo airodump-ng wlan0mon --band a` a = 5GHz | b = 2.4GHz | g = 2.4GHz
- Save output to a file: `sudo airodump-ng wlan0mon -w HTB`

# Airgraph-ng
Python script designed for generating graphical representations of wireless networks using the CSV files produced by Airodump-ng. These CSV files from Airodump-ng capture essential data regarding the associations between wireless clients and Access Points (APs), as well as the inventory of probed networks. Airgraph-ng processes these CSV files to produce two distinct types of graphs:
- Clients to AP Relationship Graph (CARP): This graph illustrates the connections between wireless clients and Access Points, providing insights into the network topology and the interactions between devices.
- Clients Probe Graph (CPG): This graph showcases the probed networks by wireless clients, offering a visual depiction of the networks scanned and potentially accessed by these devices.
e.g
<img width="765" height="276" alt="image" src="https://github.com/user-attachments/assets/8290773f-8f37-4d9d-a05f-bcbe5ede769f" />
- Green for WPA
- Yellow for WEP
- Red for open networks
- Black for unknown encryption.

Airgraph-ng Commands
- Runs off the files generated by airodump-ng, CARP: `sudo airgraph-ng -i HTB-01.csv -g CAPR -o HTB_CAPR.png`
- CPG run: `sudo airgraph-ng -i HTB-01.csv -g CPG -o HTB_CPG.png`

## Aireplay-ng
The primary function of Aireplay-ng is to generate traffic for later use in aircrack-ng for cracking the WEP and WPA-PSK keys. There are different attacks that can cause deauthentication for the purpose of capturing WPA handshake data, fake authentications, Interactive packet replay, hand-crafted ARP request injection, and ARP-request reinjection. With the packetforge-ng tool it's possible to create arbitrary frames.

Aireply-ng Commands
- Basic Usage: `aireplay-ng` <-- will show you what attacks available

Testing for Packet Injection
Before sending deauthentication frames, it's important to verify if our wireless card can successfully inject frames into the target access point (AP). This can be tested by measuring the ping response times from the AP, which gives us an indication of the link quality based on the percentage of responses received. Furthermore, if we are using two wireless cards, this test can help identify which card is more effective for injection attacks.
- `sudo iw dev wlan0mon set channel 1` (Only after card is in monitor mode)
- `sudo aireplay-ng --test wlan0mon` | Should see ` Injection is working!`

Aireplay-ng for Deauth
- View available networks: `sudo airodump-ng wlan0mon`
-Deauth: `sudo aireplay-ng -0 5 -a 00:14:6C:7A:41:81 -c 00:0F:B5:32:31:31 wlan0mon` -a = access point | -c = client (victim)
```
-0 means deauthentication
5 is the number of deauths to send (you can send multiple if you wish); 0 means send them continuously
-a 00:14:6C:7A:41:81 is the MAC address of the access point
-c 00:0F:B5:32:31:31 is the MAC address of the client to deauthenticate; if this is omitted then all clients are deauthenticated
wlan0mon is the interface name
```
Once the clients are deauthenticated from the AP, we can continue observing airodump-ng to see when they reconnect: `sudo airodump-ng wlan0mon`. In the output, we will see that after sending the deauthentication packet, the client disconnects and then reconnects. This is evidenced by the increase in Lost packets and Frames count.

Additionally, a four-way handshake would be captured by airodump-ng, as shown in the output. By using the -w option in airodump-ng, we can save the captured WPA handshake into a .pcap file. This file can then be used with tools like aircrack-ng to crack the pre-shared key (PSK). 

## Airdecap-ng
Airdecap-ng is a valuable tool for decrypting wireless capture files once we have obtained the key to a network. It can decrypt WEP, WPA PSK, and WPA2 PSK captures. Additionally, it can remove wireless headers from an unencrypted capture file. This tool is particularly useful in analyzing the data within captured packets by making the content readable and removing unnecessary wireless protocol information. Airdecap-ng can be used for the following:
- Removing wireless headers from an open network capture (Unencrypted capture).
- Decrypting a WEP-encrypted capture file using a hexadecimal WEP key.
- Decrypting a WPA/WPA2-encrypted capture file using the passphrase.

Airdecap-ng will generate a new file with the suffix -dec.cap, which contains the decrypted or stripped version of the original input file. For instance, an input file named HTB-01.cap will result in an unencrypted output file named HTB-01-dec.cap.

Airdecap-ng Commands
usage: `airdecap-ng [options] <pcap file>`

| Option | Description                                      |
|--------|--------------------------------------------------|
| -l     | don't remove the 802.11 header                   |
| -b     | access point MAC address filter                  |
| -k     | WPA/WPA2 Pairwise Master Key in hex              |
| -e     | target network ascii identifier                  |
| -p     | target network WPA/WPA2 passphrase               |
| -w     | target network WEP key in hexadecimal            |

- To remove the wireless headers from the capture file using Airdecap-ng: `airdecap-ng -b <bssid> <capture-file>` e.g `sudo airdecap-ng -b 00:14:6C:7A:41:81 opencapture.cap`.
- Decrypting WEP-encrypted captures (Once we have obtained the hexadecimal WEP key): `airdecap-ng -w <WEP-key> <capture-file>`. e.g `sudo airdecap-ng -w 1234567890ABCDEF HTB-01.cap`
- Decrypting WPA-encrypted captures (provided we have the passphrase): `airdecap-ng -p <passphrase> <capture-file> -e <essid>` e.g `sudo airdecap-ng -p 'abdefg' HTB-01.cap -e "Wireless Lab"`

All of these commands will produce a file with the suffix `-dec.cap`)

Example of `airodump-ng` pcap:
<img width="1447" height="527" alt="image" src="https://github.com/user-attachments/assets/800c9bb4-700c-4e9f-8f50-047d9f41723b" />

Example of same pcap decrpyted with airdecap-ng:
<img width="1493" height="536" alt="image" src="https://github.com/user-attachments/assets/9ba8899b-e871-49b8-9509-f0db079f8365" />


## Aircrack-ng
Tool designed for network security testing, capable of cracking WEP and WPA/WPA2 networks that use pre-shared keys or PMKID. Aircrack-ng is an offline attack tool, as it works with captured packets and doesn't need direct interaction with any Wi-Fi device. To test the abilities of your PC run: `aircrack-ng -S` the output will tell you how many passphrases you can crack per second. Since Aircrack-ng fully utilizes the CPU, the cracking speed can decrease significantly if other demanding tasks are running on the system simultaneously.

Cracking WEP
Aircrack-ng is capable of recovering the WEP key once a sufficient number of encrypted packets have been captured using Airodump-ng. It is possible to save only the captured IVs (Initialization Vectors) using the --ivs option in Airodump-ng. Once enough IVs are captured, we can utilize the -K option in Aircrack-ng, which invokes the Korek WEP cracking method to crack the WEP key.
- `aircrack-ng -K HTB.ivs`

Cracking WPA
Aircrack-ng has the capability to crack the WPA key once a "four-way handshake" has been captured using Airodump-ng. To crack WPA/WPA2 pre-shared keys, only a dictionary-based method can be employed, which necessitates the use of a wordlist containing potential passwords. A "four-way handshake" serves as the required input. For WPA handshakes, a complete handshake comprises four packets. However, Aircrack-ng can effectively operate with just two packets. Specifically, EAPOL packets 2 and 3, or packets 3 and 4, are considered a full handshake.
- ` aircrack-ng HTB.pcap -w /opt/wordlist.txt`





