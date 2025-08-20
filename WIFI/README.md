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
