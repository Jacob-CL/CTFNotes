# Cross-Site Scripting (XSS)
- XSS vulnerabilities take advantage of a flaw in user input sanitization to "write" JavaScript code to the page and execute it on the client side, leading to several types of attacks. XSS vulnerabilities are solely executed on the client-side (browser) and hence do not directly affect the back-end server. They can only affect the user executing the vulnerability.
- If a skilled researcher identifies a binary vulnerability in a web browser (e.g., a Heap overflow in Chrome), they can utilize an XSS vulnerability to execute a JavaScript exploit on the target's browser, which eventually breaks out of the browser's sandbox and executes code on the user's machine.
- XSS can be injected into any input in the HTML page, which is not exclusive to HTML input fields, but may also be in HTTP headers like the Cookie or User-Agent (i.e., when their values are displayed on the page).

| Type | Description |
|------|-------------|
| `Stored (Persistent) XSS` | The most critical type of XSS, which occurs when user input is stored on the back-end database and then displayed upon retrieval (e.g., posts or comments) |
| `Reflected (Non-Persistent) XSS` | Occurs when user input is displayed on the page after being processed by the backend server, but without being stored (e.g., search result or error message) |
| `DOM-based XSS` | Another Non-Persistent XSS type that occurs when user input is directly shown in the browser and is completely processed on the client-side, without reaching the back-end server (e.g., through client-side HTTP parameters or anchor tags) |

- Also blind: A Blind XSS vulnerability occurs when the vulnerability is triggered on a page we don't have access to. e.g Contact forms, reviews, user details, support tickets, http user-agent header.
- How would we be able to detect an XSS vulnerability if we cannot see how the output is handled? Try testing various remote script XSS payloads with the remaining input fields, and see which of them sends an HTTP request to find a working payload via a using netcat or php listener

- Stored is the most critical - If our injected XSS payload gets stored in the back-end database and retrieved upon visiting the page, this means that our XSS attack is persistent and may affect any user that visits the page.
- Reflected XSS vulnerabilities occur when our input reaches the back-end server and gets returned to us without being filtered or sanitized. There are many cases in which our entire input might get returned to us, like error messages or confirmation messages. 
- But if the XSS vulnerability is Non-Persistent, how would we target victims with it? ..to target a user, we can send them a URL containing our payload. 
- DOM XSS occurs when JavaScript is used to change the page source through the Document Object Model (DOM). NO HTTP requests are made in the netwrok tab of devtools - This indicates that the input is being processed at the client-side through JavaScript and never reaches the back-end; hence it is a DOM-based XSS.
- To further understand the nature of the DOM-based XSS vulnerability, we must understand the concept of the Source and Sink of the object displayed on the page. The Source is the JavaScript object that takes the user input, and it can be any input parameter like a URL parameter or an input field, as we saw above.
- On the other hand, the Sink is the function that writes the user input to a DOM Object on the page. If the Sink function does not properly sanitize the user input, it would be vulnerable to an XSS attack. Some of the commonly used JavaScript functions to write to DOM objects are:
    - document.write()
    - DOM.innerHTML
    - DOM.outerHTML
- Furthermore, some of the jQuery library functions that write to DOM objects are:
    - add()
    - after()
    - append()
- If a Sink function writes the exact input without any sanitization (like the above functions), and no other means of sanitization were used, then we know that the page should be vulnerable to XSS.

## Automated Discovery
- https://www.tenable.com/products/nessus | https://portswigger.net/burp/pro | https://www.zaproxy.org/
- Opensource Tools: https://github.com/s0md3v/XSStrike | https://github.com/rajeshmajumdar/BruteXSS | https://github.com/epsylon/xsser
 

# XSS Testing Payloads
- `<marquee>` | `<script>alert(window.origin)</script>`
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md | https://github.com/payloadbox/xss-payload-list

## Defacing
- Four HTML elements are usually utilized to change the main look of a web page:
    - Background Color document.body.style.background (`<script>document.body.style.background = "#141d2b"</script>`)
    - Background document.body.background (`<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>`)
    - Page Title document.title (`<script>document.title = 'HackTheBox Academy'</script>`)
    - Page Text DOM.innerHTML (`document.getElementById("todo").innerHTML = "New Text"` | `$("#todo").html('New Text');`

## Phishing
- A common form of XSS phishing attacks is through injecting fake login forms that send the login details to the attacker's server, which may then be used to log in on behalf of the victim and gain control over their account and sensitive information.
- Login form injection with HTML, `http://SERVER_IP/phishing/index.php?url=<script>alert(window.origin)</script>`, POST data to netcat listener

## Session Hijacking
- Cookies maintian a users session, we want to steal it to hijack their session
