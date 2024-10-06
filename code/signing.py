# signing.py
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def sign_message(message, private_key):
    """Sign the message using the provided private key."""
    hash_message = SHA256.new(message)
    sender_private_key = RSA.import_key(private_key)
    signature = pkcs1_15.new(sender_private_key).sign(hash_message)
    return signature

def verify_signature(message, signature, public_key):
    """Verify the message's signature using the provided public key."""
    hash_message = SHA256.new(message)
    sender_public_key = RSA.import_key(public_key)
    try:
        pkcs1_15.new(sender_public_key).verify(hash_message, signature)
        return True
    except (ValueError, TypeError):
        return False
