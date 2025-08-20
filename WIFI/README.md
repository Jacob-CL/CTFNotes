# WI-FI CODE SNIPPETS
```
iwconfig
```
### Start interface in monitor mode:
```
 sudo airmon-ng start wlan1
```
### Stop monitor mode:
```
sudo airmon-ng stop wlan0mon
```
### If things are weird:
```
sudo airmon-ng check
```
```
sudo airmon-ng check kill
```
### List networks:
```
sudo iwlist wlan0 s | grep 'Cell\|Quality\|ESSID\|IEEE'
```
Dump network traffic to file: (airodump-ng is configured to scan exclusively for networks operating on the 2.4 GHz band so use `--band abg` if necessary
```
sudo airodump-ng wlan1mon --band a -w dump
```
Visualize APs and Clients with: (Use airodump-ng .csvs)
```
sudo airgraph-ng -i HTB-01.csv -g CAPR -o HTB_CAPR.png
```
OR for CPG:
```
sudo airgraph-ng -i HTB-01.csv -g CPG -o HTB_CPG.png
```
Rasberry Pi MAC address ranges:
```
28:CD:C1:xx:xx:xx
B8:27:EB:xx:xx:xx
D8:3A:DD:xx:xx:xx
DC:A6:32:xx:xx:xx
E4:5F:01:xx:xx:xx
```

---

## Install Alpha Adapter
Configuring the Alpha AWUS036ACH Wi-Fi Adapter - [Link](https://medium.com/@wicked_picker/configuring-the-alpha-awus036ach-wi-fi-adapter-on-kali-linux-eb5ec2826713)
See available USBs:
```
lsusb
```
Then see it NOT here:
```
iwconfig
```
Install the Realtek drivers:
```
sudo apt-get install realtek-rtl88xxau-dkms
```
Install dkms:
```
sudo apt-get install dkms
```
Download the rtl8812au drivers from GitHub
```
git clone https://github.com/aircrack-ng/rtl8812au
```
```
cd rtl8812au
```
Preemptively fix the error:
```
sudo apt-get install linux-headers-$(uname -r)
```
```
make
```
```
sudo make install
```
```
reboot
```
```
iwconfig
```

---


