# Code breaking
- UPPERCASE = ciphertext
- lowercase = plaintext
- Average word length = 6.2
- Index of coincidence = 6.7%

## Most frequent digrams / trigraphs
1. TH
2. HE
3. IN
4. ER
5. AN
6. RE
7. ND
8. AT
9. ON
10. NT

## Most frequent trigrams / trigraphs
1. THE
2. AND
3. THA
4. ENT
5. ING
6. ION
7. TIO
8. FOR
9. NDE
10. HAS

## Most frequent double letters
1. LL
2. TT
3. SS
4. EE
5. PP
6. OO
7. RR
8. FF
9. CC
10. DD

## Most frequent words
1. THE
2. OF
3. AND
4. TO
5. A
6. IN
7. THAT
8. IT
9. IS
10. I

## Index of Coincidence
The Index of Coincidence is like a "randomness detector" for text. It tells you how "English-like" a piece of text looks.
- IoC ≈ 0.067 = Normal English text
- IoC ≈ 0.038 = Random/encrypted text

IoC calculation uses these single letter counts and is included in `frequency_analyzer.py`

If you have encrypted text with IoC around 0.067, you know it's probably a simple substitution cipher / caesar that you can crack. If it's around 0.038, it's either good encryption or a more complex cipher.