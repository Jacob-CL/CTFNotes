def rot_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

encrypted_text = "xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}"


for shift in range(1, 26):
    print(f"ROT{shift}: {rot_cipher(encrypted_text, shift)}")