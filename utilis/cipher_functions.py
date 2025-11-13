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
    decrypted_text = text[::2]
    decrypted_text += text[::2]

    return decrypted_text


