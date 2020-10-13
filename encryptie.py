__author__ = 'David'

from Crypto.Cipher import AES
import base64

ENCRYPTION_KEY = "DiT_is_|Y|y|\|_w8w00rd"

# Bron: https://gist.github.com/LoyVanBeek/5264046
BLOCK_SIZE = 32
PADDING = '{'

def pad(s):
	return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

def EncodeAES(plaindata, key):
	key = pad(key)
	cipher = AES.new(key)
	enc = cipher.encrypt(pad(plaindata))
	return base64.b64encode(enc)

def DecodeAES(encodeddata, key):
	key = pad(key)
	cipher = AES.new(key)
	b64 = base64.b64decode(encodeddata)
	return cipher.decrypt(b64)

# encoded = EncodeAES('password', ENCRYPTION_KEY)
# print('Encrypted string:', encoded)
#
# # decode the encoded string
# print('Correctly   decrypted string:', DecodeAES(encoded, ENCRYPTION_KEY))