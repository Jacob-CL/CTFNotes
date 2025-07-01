# Javascript Obfuscation
- HTML is used to determine the website's main fields and parameters, and CSS is used to determine its design, JavaScript is used to perform any functions necessary to run the website. 
- JavaScript can be internally written between `<script>` elements or written into a separate .js file and referenced within the HTML code e.g `<script src="secret.js"></script>` although it's usually obfuscated.
- While Python and PHP usually reside on the server-side and hence are hidden from end-users, JavaScript is usually used within browsers at the client-side, and the code is sent to the user and executed in cleartext. This is why obfuscation is very often used with JavaScript.
- authentication or encryption on the client-side is not recommended, as code is more prone to attacks this way.
- Obfuscation is also used maliciously to hide malware functions etc
- Run Javascript: https://jsconsole.com/
- A common way of reducing the readability of a snippet of JavaScript code while keeping it fully functional is JavaScript minification. Code minification means having the entire code in a single (often very long) line. 
- https://www.toptal.com/developers/javascript-minifier
- Deobfuscate tools: `https://beautifytools.com/javascript-obfuscator.php` | `https://obfuscator.io/` | `https://jsfuck.com/`
- A packer obfuscation tool usually attempts to convert all words and symbols of the code into a list or a dictionary and then refer to them using the (p,a,c,k,e,d) function to re-build the original code during execution.
- While a packer does a great job reducing the code's readability, we can still see its main strings written in cleartext, which may reveal some of its functionality. This is why we may want to look for better ways to obfuscate our code.
- Obfuscators can make code execution slow if it's really convaluted.

## Deobfuscation
- If we need to reverse minification, we need to `Beautify` or `Pretty Print` our code. The most basic method for doing so is through our Browser Dev Tools. Look for the {} at the bottom of dev tools.
- Also can use: `https://prettier.io/playground/` | `https://beautifier.io/` | `https://matthewfl.com/unPacker.html`
- Ensure you do not leave any empty lines before the script, as it may affect the deobfuscation process and give inaccurate results.
- We might need to reverse engineer the obfuscated JS if there's been a custom obfuscatred tool used or a tonne has been applied making the de-ob tools inefficient / useless

## Code Analysis
- Google / GPT Javascript functions you don't know
- If it's making HTTPS requests, use cURL to poke at the endpoints the JS is GET or POSTing to

## Decoding
- 3 common test encoding methods: base64 | hex | rot13
- base64 pads with `=`
- To encode any text into base64 in Linux, we can echo it and pipe it with `|` to base64: `echo https://www.hackthebox.eu/ | base64`
- If we want to decode any base64 encoded string, we can use base64 -d, as follows: `echo aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K | base64 -d`
- Hex: Any string encoded in hex would be comprised of hex characters only, which are 16 characters only: 0-9 and a-f. That makes spotting hex encoded strings just as easy as spotting base64 encoded strings.
- To encode any string into hex in Linux, we can use the xxd -p command: `echo https://www.hackthebox.eu/ | xxd -p`
- To decode a hex encoded string, we can use the xxd -p -r command: `echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r`
- rot13 is a Caesar Cipher than shifts characters 13 times forward.
- Spotted easily with pattern recognition. For example, `http://www` becomes `uggc://jjj`, which still holds some resemblances and may be recognized as such.
- Not easily done in linux but `echo https://www.hackthebox.eu/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- We can use the same previous command to decode rot13 as well: `echo uggcf://jjj.unpxgurobk.rh/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- Many many many different types of encoding, try https://www.boxentriq.com/code-breaking/cipher-identifier.




