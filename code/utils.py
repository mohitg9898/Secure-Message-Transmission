# utils.py
#pip install pycryptodome
from Crypto.PublicKey import RSA

def generate_rsa_key_pair():
    """Generate a pair of RSA keys (private and public)."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key
