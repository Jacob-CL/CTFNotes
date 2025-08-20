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




