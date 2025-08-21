# MAC filtering bypass
MAC filtering involves allowing only devices with specific MAC (Media Access Control) addresses to connect to the network. This process typically involves MAC address spoofing, where an attacker changes their device's MAC address to match an allowed device, thereby gaining access to the network. 

We might have the right password, but there might be MAC filtering going on that will disallow us from connecting to the network. To bypass the MAC filtering, we can spoof our MAC address to match one of the connected clients. However, this approach often leads to collision events, as two devices with the same MAC address cannot coexist on the same network simultaneously.

Forcibly disconnect the legitimate client through via deatuh, thereby freeing up the MAC address for use, then connect with spoofed IP.

### NOTE
Occasionally, when configuring our MAC address to match that of a client or access point, we may encounter collision events at the data-link layer. This technique of bypassing MAC filtering is most effective when the client we're mimicking is not currently connected to our target network. However, there are instances where these collision events become advantageous to us, serving as a means of denial-of-service (DOS) attack. In the case of a dual-band or multiple access point network, we may be able to utilize a MAC address of a client connected to a separate access point within the same wireless infrastructure.

We can also check if there is a 5 GHz band available for the ESSID. If the 5 GHz band is available, we can attempt to connect to the network using that frequency, which would avoid collision events since most clients are connected to the 2.4 GHz band. If we see that a network has a 5G network, and since most devices might auto-connect to the 2.5GHz frequency, we can spook that MAC address to the 5Ghz network as long as it's not connected to it. 

```
To see MAC address:
```
sudo macchanger wlan1
```
To change MAC address:
```
sudo ifconfig wlan1 down
```
```
sudo macchanger wlan1 -m 3E:48:72:B7:62:2A
```
```
sudo ifconfig wlan1 up
```
```
sudo macchanger wlan1
```
OR:
```
ifconfig wlan1
```

```
sudo airodump-ng wlan1mon
```
Connect via GUI or CLI and verify connection with:
```
ifconfig
```
