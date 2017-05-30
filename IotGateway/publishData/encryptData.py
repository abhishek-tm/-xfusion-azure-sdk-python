'''
Created on 24-May-2016
@author: TERAMATRIX/siddhika.nag

Script to encrypt data through AES algorithm.
KEY (32 bit) -> IP&Port[0 padding]DeviceId
                eg. 192.168.1.41:1883&00000000000066
'''
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import base64
import os
#from logger import log_function
file_name = os.path.basename(__file__).split('.')[0]
#logger = log_function(file_name)

"""
    encryptData(IP,Port,DeviceId,content)
	Function to encrypt data using AES algorithm
	Parameters : IoTHub IP, Port, DeviceID and Performance Data
        Returns : Encrypted data
"""
def encryptData(IP,Port,DeviceId,content):
    encoder = PKCS7Encoder()
    secret = '{0}:{1}&{2}{3}'.format(IP,Port,'0'* (30 - (len(IP) + len(Port) + len(DeviceId))),DeviceId)
    #logger.debug('key: %s' %(secret))
    aes = AES.new(secret)
    try:
        pad_text = encoder.encode(content)
        # encrypt the padding content
        cipher_encode = aes.encrypt(pad_text)
        # base64 encode the cipher content for transport
        encrypt_cipher = base64.b64encode(cipher_encode)
        #logger.debug('Encrypted string: %s' %(encrypt_cipher ))
    except Exception, exp :
        print exp
        #logger.error('Error in encryption: %s'%(exp ))
    # base64 decode the cipher encrypt content for transport
    try:
        decodetext =  base64.b64decode(encrypt_cipher)
        cipher_decode = aes.decrypt(decodetext)
        decrypt_cipher = encoder.decode(cipher_decode)
        #logger.debug('Decrypted string: %s' %(decrypt_cipher)) 
    except Exception, exp :
        print exp
        #logger.error('Error in decryption: %s'%(exp ))
    return encrypt_cipher

