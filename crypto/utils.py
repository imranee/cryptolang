import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_random_key():
    return os.urandom(32)  # 256-bit AES key

def encrypt_text(text):
    key = generate_random_key()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    encrypted_text = base64.b64encode(cipher.iv + encrypted_bytes).decode()
    key_b64 = base64.b64encode(key).decode()
    return encrypted_text, key_b64

def decrypt_text(encrypted_text, key_b64):
    key = base64.b64decode(key_b64)
    encrypted_bytes = base64.b64decode(encrypted_text)
    iv = encrypted_bytes[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_bytes[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()