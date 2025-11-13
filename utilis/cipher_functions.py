def caesar_encryption(text: str, offset: int) -> str:
    encrypted_text = ''

    for char in text.lower():
        if char.isalpha():
            cipher_ascii_value = (ord(char) + offset) % 122
            cipher = chr(cipher_ascii_value)
            encrypted_text += cipher
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decryption(text: str, offset: int) -> str:
    encrypted_text = ''

    for char in text.lower():
        if char.isalpha():
            cipher_ascii_value = (ord(char) - offset) % 122
            cipher = chr(cipher_ascii_value)
            encrypted_text += cipher
        else:
            encrypted_text += char
    return encrypted_text


def fence_encryption(text: str) -> str:
    text_without_space = ''.join(text)
    encrypted_text = text_without_space[::2]
    encrypted_text += text_without_space[1::2]

    return encrypted_text


def fence_decryption(text: str) -> str:
    even_i = text[:(len(text) // 2) + 1]
    odd_i = text[(len(text) // 2):]
    print(even_i, odd_i)

    decrypted_text = ''

    for i in range((len(text) // 2)):
        try:
            decrypted_text += even_i[i]
            decrypted_text += odd_i[i]
        except IndexError:
            decrypted_text += even_i[i]

    return decrypted_text