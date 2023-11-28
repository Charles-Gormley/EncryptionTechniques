from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64

def generate_keys():
    # key length must be a multiple of 256 and >= 1024
    modulus_length = 2048  # use 1024, 2048 or 4096
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

# Generate keys
def encrypt_message(message, publickey):
    message = message.encode('utf-8')
    cipher = PKCS1_OAEP.new(publickey)
    encrypt_message = cipher.encrypt(message)
    encoded_encrypted_msg = base64.b64encode(encrypt_message)
    return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    cipher = PKCS1_OAEP.new(privatekey)
    decoded_decrypted_msg = cipher.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg.decode('utf-8')

def square_and_mulitply(x, e, m):
    publickey_binary = bin(e)[2:]
    r = 1
    for bit in publickey_binary:
        r = (r ** 2) % m
        if (bit == '1'):
            r = (r * x) % m
    return r

if __name__ == "__main__":
    MESSAGE = 'This is a test message'
    privatekey, publickey = generate_keys()
    encrypted_msg = encrypt_message(MESSAGE, publickey)
    decrypted_msg = decrypt_message(encrypted_msg, privatekey)
    
    print("Private Key: %s - (%d)" % (privatekey.exportKey(), len(privatekey.exportKey())))
    print("Public  Key: %s - (%d)" % (publickey.exportKey(), len(publickey.exportKey())))
    print("Original content: %s - (%d)" % (MESSAGE, len(MESSAGE)))
    print("Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg)))
    print("Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg)))


