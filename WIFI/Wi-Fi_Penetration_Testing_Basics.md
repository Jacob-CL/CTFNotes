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
