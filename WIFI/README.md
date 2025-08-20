# WI-FI CODE SNIPPETS
```
iwconfig
```
Start interface in monitor mode:
```
 sudo airmon-ng start wlan0
```
Stop monitor mode:
```
sudo airmon-ng stop wlan0mon
```
If things are weird:
```
sudo airmon-ng check
```
```
sudo airmon-ng check kill
```
List networks:
```
sudo iwlist wlan0 s | grep 'Cell\|Quality\|ESSID\|IEEE'
```
Rasberry Pi MAC address ranges:
```
28:CD:C1:xx:xx:xx
B8:27:EB:xx:xx:xx
D8:3A:DD:xx:xx:xx
DC:A6:32:xx:xx:xx
E4:5F:01:xx:xx:xx
```
