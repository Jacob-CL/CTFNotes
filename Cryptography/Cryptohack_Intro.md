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

## Bytes and Big Integers
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:
```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```
Python's PyCryptodome library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`

Convert the following integer back into a message:
```
11515195063862318899931685488813747395775516287289682636499965282714637259206269
```
```
>>> CIPHER= 11515195063862318899931685488813747395775516287289682636499965282714637259206269
>>> CIPHER_BYTES = long_to_bytes(CIPHER)
>>> print(CIPHER_BYTES)
```
- [Crypto.Util.number-module](https://pythonhosted.org/pycrypto/Crypto.Util.number-module.html)

### Why is it important to convert the long to bytes?
Cryptographic Operations Work on Numbers, But Data is Bytes.
- RSA and other crypto systems perform mathematical operations on large integers
- But the original meaningful data (messages, files, flags) exists as bytes
- You need to convert back to bytes to get the human-readable result

e.g `11515195063862318899931685488813747395775516287289682636499965282714637259206269` as a long data type is useless, but when converted to bytes, those bytes represent ASCII characters which can form a readable flag/message. Without byte conversion: You just have a giant useless number.

## XOR Starter
XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret `^` used instead.

| A | B | Output | 
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

For longer binary numbers we XOR bit by bit: `0110 ^ 1010 = 1100`. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string `label`, XOR each character with the integer `13`. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

The Python `pwntools` library has a convenient `xor()` function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.

Version without pwntools:
```
>>> # Given string and key
... text = "label"
... key = 13
... 
... # XOR each character
... result = ""
... for char in text:
...     # Get ASCII value, XOR with key, convert back to character
...     xored_char = chr(ord(char) ^ key)
...     result += xored_char
... 
... print(f"crypto{{{result}}}")
```
- Each character in "label" gets converted to its ASCII value
- That value gets XORed with 13
- The result gets converted back to a character
- All the XORed characters form your flag
- Version with pwntools:
```
from pwn import xor

# Given string and key
text = "label"
key = 13

# XOR using pwntools
result = xor(text.encode(), key).decode()

print(f"crypto{{{result}}}")
```








