# Intro course
## ASCII
- [Conversion Table](https://www.rapidtables.com/code/text/ascii-table.html)
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
```
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```
In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite). e.g `
```
numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ""
for num in numbers:
    flag += chr(num)

print(flag)
```
```
chmod +x intro.py; python3 intro.py
```
- [chr()](https://www.w3schools.com/python/ref_func_chr.asp): The `chr()` function returns the character that represents the specified unicode.
```
>>> x = chr(97)
>>> print(x)
a
```

## Hex
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.
```
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```
In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.
```
>>> cipher = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
>>> plaintext = bytes.fromhex(cipher)
>>> print(plaintext)
```
- [bytes.fromhex()](https://www.geeksforgeeks.org/python/convert-hex-string-to-bytes-in-python/)

## Base64
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.
```
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
```
In Python, after importing the base64 module with `import base64`, you can use the `base64.b64encode()` function. Remember to decode the hex first as the challenge description states.
```
>>> CIPHERTEXT = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
>>> CIPHERTEXT_BYTES = bytes.fromhex(CIPHERTEXT)
>>> plaintext = base64.b64encode(CIPHERTEXT_BYTES)
>>> print(plaintext)
```

