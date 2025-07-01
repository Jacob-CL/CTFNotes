# Attacking Web Apps with Ffuf
- https://github.com/ffuf/ffuf
- Fuzzing for: directories, files and extensions, hidden vhosts, PHP parameters + parameter values
- Needs effective use of wordlists: `/usr/share/wordlists/seclists`

## Directory Fuzzing
- Main two options are `-w` for wordlists and `-u` for the URL
- We can pick our wordlist and assign the keyword FUZZ to it by adding :FUZZ after it: `ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ`
- Then we can place the FUZZ keyword where the directory would be within our URL, with: `ffuf -w <SNIP> -u http://SERVER_IP:PORT/FUZZ`
- A full command looks like: `ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ`
- `threads` flag (`-t`) will speed or slow it down

## Page Fuzzing
- One common way to identify that is by finding the server type through the HTTP response headers and guessing the extension.
- Apache likely means `.php`, IIS then likely `.as` or `.aspx
- `ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/blog/indexFUZZ`
- If the above command gives you a 200 on some index.php then you know it's a php website.
- And thus we can do a new ffuf command to fuzz for `.php` files: `ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php`

## Recursive Fuzzing
- We can scan recursively for super long paths like `login/user/content/uploads/...etc` with the `recursion` flag.
- We can specify the depth with the `-recursion-depth` flag.
- e.g `ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v`

## DNS Records
- The reason we add the HTB URL to the etc/hosts files is because they are not public and therefore the DNS never resolves.

## Sub-domain Fuzzing
- For example, https://photos.google.com is the `photos` sub-domain of google.com.
- Need a target (`-u`) + wordlist (`-w`) e.g `ffuf -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.inlanefreight.com/`
- If we run something like the above command and get no results this could just mean that there are no **public** sub-domains under academy.htb, as it does not have a public DNS record, as previously mentioned. We may have added academy.htb to our /etc/hosts file, we only added the main domain, so when ffuf is looking for other sub-domains, it will not find them in /etc/hosts, and will ask the public DNS, which obviously will not have them.

##Vhost Fuzzing
- The key difference between VHosts and sub-domains is that a VHost is basically a 'sub-domain' served on the same server and has the same IP, such that a single IP could be serving two or more different websites.
- VHosts may or may not have public DNS records.
- To scan for VHosts, without manually adding the entire wordlist to our /etc/hosts, we will be fuzzing HTTP headers, specifically the Host: header. To do that, we can use the -H flag to specify a header and will use the FUZZ keyword within it, as follows: `ffuf -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb'`
- Expect 200s because we're hitting an IP that we know exists, but the clues are in the response lengths.

## Filtering results 
- `-fs` for response/file size

## Parameter fuzzing - GET
- If the page is saying we don't have access, there must be something that identifies users to verify whether they have access or not. That's either a login, cookie or some key that we can pass to the page. Such keys would usually be passed as a parameter, using either a GET or a POST HTTP request.
- Fuzzing parameters may expose unpublished parameters that are publicly accessible. Such parameters tend to be less tested and less secured, so it is important to test such parameters for the web vulnerabilities we discuss in other modules.
- GET requests are usually passed right after the URL, with a ? symbol, like: `http://admin.academy.htb:PORT/admin/admin.php?param1=key`
- Replace `param1` in the example with FUZZ: `ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx`

## Paramter Fuzzing - POST
- The main difference between POST requests and GET requests is that POST requests are not passed with the URL and cannot simply be appended after a ? symbol.
- To fuzz the data field with ffuf, we can use the -d flag, we also have to add -X POST to send POST requests.
- In PHP, `POST` data `content-type` can only accept `application/x-www-form-urlencoded`. So, we can set that in "ffuf" with "-H 'Content-Type: application/x-www-form-urlencoded'".
- e.g `ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`

## Value Fuzzing
- After fuzzing a working parameter, we now have to fuzz the correct value of that parameter. 
- When it comes to fuzzing parameter values, we may not always find a pre-made wordlist that would work for us, as each parameter would expect a certain type of value. For keys, think what else the website might be using for keys like 5 digit numbers etc.
- e.g `ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`
