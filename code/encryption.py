# encryption.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(message, public_key):
    recipient_public_key = RSA.import_key(public_key)
    cipher_rsa_encrypt = PKCS1_OAEP.new(recipient_public_key)
    encrypted_message = cipher_rsa_encrypt.encrypt(message)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    recipient_private_key = RSA.import_key(private_key)
    cipher_rsa_decrypt = PKCS1_OAEP.new(recipient_private_key)
    decrypted_message = cipher_rsa_decrypt.decrypt(encrypted_message)
    return decrypted_message
