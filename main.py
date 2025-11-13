import json
from fastapi import FastAPI

from utilis.cipher_functions import caesar_encryption, caesar_decryption, fence_encryption, fence_decryption
from utilis.item_models import CaesarItem, FenceToDecryptItem
from utilis.util_functions import save_to_file

app = FastAPI()

@app.get('/test')
def msg_from_server():
    return {"msg": "hi from test"}

@app.get('/test/{name}')
def save_name(name: str):
    save_to_file(name)

    return json.dumps({"msg": "saved user"})

@app.post('/caesar')
def caesar_cipher(item: CaesarItem):
    if item.mode == 'encrypt':
        encrypted_text = caesar_encryption(item.text, item.offset)
        return json.dumps({"encrypted_text": encrypted_text})
    elif item.mode == 'decrypt':
        decrypted_text = caesar_decryption(item.text, item.offset)
        return json.dumps({"decrypted_text": decrypted_text})
    else:
        return json.dumps({"msg": "not correct typing for 'mode'."})

@app.get('/fence/encrypt')
def fence_encrypt(text: str):
    encrypted_text = fence_encryption(text)

    return json.dumps({"encrypted_text": encrypted_text})


@app.post('/fence/decrypt')
def fence_decrypt(item: FenceToDecryptItem):
    decrypted_text = fence_decryption(item.text)

    return json.dumps({"decrypted_text": decrypted_text})











