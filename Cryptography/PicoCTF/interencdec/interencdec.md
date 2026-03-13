# interencdec
- Base64 decode x 2, then caesar cipher -7


encoded flag given to you = YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==

```
>>> import base64
>>> encoded = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg=="
>>> decoded = base64.b64decode(encoded).decode("utf-8")
>>> print(decoded)
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='
```
Decode new string:
```
new_encoded = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=="
>>> decoded2 = base64.b64decode(new_encoded).decode("utf-8")
>>> print(decoded2)
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}
```
This is a Caesar Cipher `-7`: picoCTF{caesar_d3cr9pt3d_86de32d2}