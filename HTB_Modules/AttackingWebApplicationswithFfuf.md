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
