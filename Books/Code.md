# Code: The Hidden Language of Computer Hardware and Software: Second Edition
### by Charles Petzold.

# Chapter 1
- 3 dots, 3 dashes, 3 dots = SOS in morse code
- Those dots and dashes (2 types of blinks, 3 types of vowel sounds, 2 different anything can with suitable combinations convey all types of information

# Chapter 2

<img width="774" height="713" alt="image" src="https://github.com/user-attachments/assets/4d4757a8-9d0b-47d3-8f74-4cad0a6cc0d7" />

<img width="757" height="516" alt="image" src="https://github.com/user-attachments/assets/061bd8f6-1c5f-4ecb-9f01-428510909fca" />

<img width="660" height="724" alt="image" src="https://github.com/user-attachments/assets/64b06415-2c22-4c80-a592-8b10218db7ed" />

- number of codes = 2^^number of dots and dashes

<img width="496" height="441" alt="image" src="https://github.com/user-attachments/assets/fc04c619-141d-4d5c-86b7-40dda5232e6e" />

- Morse code is said to be binary (literally meaning two by two) because the components of the code consist of only 2 things - a dot and a dash. That's similar to a coin, which can land only on the head side or the tail side. Coins are flipped ten times can have 1024
different sequences of heads or tails. Combinations of binary objects (such as coins) and binary codes (such as Morse code) are always described by powers of two.
- Two is a very important number in this book.

# Chapter 3
- Braille is the only way to read for people who are both blind and deaf.
- Braille is 6 dots which can be eother ON or OFF, therefore Braille is capable of representing 64 unique codes: 2^^6 = 64. So 64 different combinations/symbols that represent Braille. If it was 8 dots, it would be 2^^8 (and then 256 symbols). If there were 3 types of dots then it would be 3^^6
- An error that occurs as a code is written is called an ENCODING error.
- An error made reading the code is called a DECODING error.
- Transmission errors occur when something like the page containing the Braille is damaged in some way making it unreadable.
- Grade 2 Braille is most widely used.
- Many of the 64 Braille symbols double up and so indicator symbols alter the meaning of the codes that follow them - from letters to numbers and from numbers back to letters. These are called PRECEDENCE or SHIFT codes. They alter the meaning of all subsequent codes until until the shift is undone. It's very similar to holding down the shift key on a computer keyboard, and its so named because the equivalent key on old type writters mechanically shifted the mechanism to type uppercase letters.
- The Braille capital indicator means that the following letter (and only the following letter) should be uppercase rather than lowercase. A code such as this is known as an escape code. Escape codes let you “escape” from the normal interpretation of a code and interpret it differently. Shift codes and escape codes are common when written languages are represented by binary codes, but they can introduce complexities because individual codes can’t be interpreted on their own without knowing what codes came before.

# Chapter 4, 5, 6, 7

# Chapter 8
- Reduced to it's essentials, a computer is a synthesis of Boolean algebra and electricity. The crucial components that embody this melding of math and hardware are known as logic gates.
- AND
<img width="448" height="132" alt="image" src="https://github.com/user-attachments/assets/29b10b72-58df-4332-8e49-0f0c065895e2" />

<img width="697" height="288" alt="image" src="https://github.com/user-attachments/assets/8661491a-7446-4b91-8526-158d5f5d0a5d" />

<img width="302" height="179" alt="image" src="https://github.com/user-attachments/assets/f1504210-f102-4d82-b5ea-5c5f802ccb12" />

- OR
<img width="454" height="127" alt="image" src="https://github.com/user-attachments/assets/2a53a164-22a1-47a9-bc42-a4a83efe91fd" />

<img width="702" height="290" alt="image" src="https://github.com/user-attachments/assets/e35faf32-0d2c-4001-9dfb-379ec9ff8857" />

<img width="257" height="161" alt="image" src="https://github.com/user-attachments/assets/c1011916-e3b9-4a6e-bcde-4f4cc6dc7afb" />

- INVERTER
<img width="708" height="313" alt="image" src="https://github.com/user-attachments/assets/90f68c44-15eb-48d1-bf2f-24ed039a6c0d" />

- NOR (NOT OR)
<img width="472" height="123" alt="image" src="https://github.com/user-attachments/assets/47d469ee-a103-4977-9972-979d7e6e9f58" />

<img width="533" height="376" alt="image" src="https://github.com/user-attachments/assets/f886f70d-0e82-41bf-85be-16812b830d07" />

- NAND (NOT AND)
<img width="472" height="126" alt="image" src="https://github.com/user-attachments/assets/0d7d5e01-1fe8-4da3-a38a-f3ef25c77478" />

<img width="476" height="213" alt="image" src="https://github.com/user-attachments/assets/34919152-e7ca-4426-af08-676aa6aae7aa" />

<img width="609" height="849" alt="image" src="https://github.com/user-attachments/assets/56b62c69-6f2b-4252-8662-9859659803fd" />

- BUFFER
<img width="763" height="208" alt="image" src="https://github.com/user-attachments/assets/6097754a-11f2-40be-afb3-7c7a55a6cecc" />

<img width="241" height="156" alt="image" src="https://github.com/user-attachments/assets/161304fb-bd20-4e86-bdb2-3a930deb0880" />

- The little circle inverts the signal
<img width="765" height="401" alt="image" src="https://github.com/user-attachments/assets/d4870c4f-e6c5-4f44-9a9a-e1a2cf843451" />

<img width="693" height="385" alt="image" src="https://github.com/user-attachments/assets/1d67d1a7-ca58-44e6-b1e8-945ce5f520ed" />

- If it's not raining AND it's not snowing, then it's not raining OR snowing.
- If I'm not big OR I'm not strong, then I'm not big AND strong.

# Chapter 9
- We use a base 10 number system but that's completely arbituary and likely because we've got 10 fingers. Ten years is a decade; ten decades is a century; ten centuries is a millennium. A thousand thousands is a million; a thousand millions is a billion.
- The number system we use today id known as the Hindu-Arabic or Indo-Arabic. It is of Indian origin but was brought to Europe by the Arab Mathematicians.
- The Hindu-Arabic System is said to be positional which means that a particular digit represents a different quantity depenedning on where it is found in the number. WHERE digits appear in the number is actually more significant than the digits themselves! Both 100 and 1000000 have only a dsingle 1 in them, yet we all know that a million is much larger than a hundred.
- Virtually all eaarly number systems have something that the Hindu-Arabic system does NOT have, and that's a special symbol for the number 10. In our number system, there's NO special symbol for ten. BUT all early number systems are missing 0, which the Hindu-Arabic system does have.

<img width="738" height="439" alt="image" src="https://github.com/user-attachments/assets/0d0044ee-fe40-4c20-90e2-cd7484c5d839" />

# Chapter 10
- We use decimal/base 10
- You can avoid some confusion if you pronounce a numeral like 10 as ONE ZERO (or 13 ike ONE THREE etc). Because remember, 0 is a placeholder. This is base 8 or octal numbers, so 10 is refering to the number of fingers cartoon characters have.

<img width="577" height="358" alt="image" src="https://github.com/user-attachments/assets/7145599f-fe64-4434-a80b-5b4537bd85dc" />

<img width="787" height="776" alt="image" src="https://github.com/user-attachments/assets/3d055d85-4f7f-433a-b989-32bc9f909d3b" />

- In an octal system:

<img width="709" height="370" alt="image" src="https://github.com/user-attachments/assets/5ae3a3d2-091e-45c6-bdf2-78a8432a9b91" />

- In a binary system:

<img width="770" height="881" alt="image" src="https://github.com/user-attachments/assets/2ebb59e4-626b-42e2-aabe-8e81fc68ca48" />

<img width="612" height="172" alt="image" src="https://github.com/user-attachments/assets/b1a69971-d6af-469d-a253-502932033a7b" />

<img width="673" height="284" alt="image" src="https://github.com/user-attachments/assets/6e0a96b8-b77e-474d-9836-67c975a12b27" />

<img width="706" height="398" alt="image" src="https://github.com/user-attachments/assets/3658033e-1dea-42c6-b684-a624d2bec656" />

# Chapter 11

















