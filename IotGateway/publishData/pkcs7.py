'''
Created on 27-Apr-2017

@author: TERAMATRIX\rupam.kumari
'''
import binascii
import StringIO
class PKCS7Encoder(object):
    '''
    RFC 2315: PKCS#7 page 21
    Some content-encryption algorithms assume the
    input length is a multiple of size octets, where size > 1, and
    let the application define a method for handling inputs
    whose lengths are not a multiple of size octets. For such
    algorithms, the method shall be to pad the input at the
    trailing end with size - (text_lenght mod size) octets all having value size -
    ( text_lenght mod size), where text_lenght is the length of the input. In other
    words, the input is padded at the trailing end with one of
    the following strings:
             01 -- if text_lenght mod size = size-1
            02 02 -- if text_lenght mod size = size-2
                        .
                        .
                        .
          size size ... size size -- if text_lenght mod size = 0
    The padding can be removed unambiguously since all input is
    padded and no padding string is a suffix of another. This
    padding method is well-defined if and only if size < 256;
    methods for larger size are an open issue for further study.
    '''
    def __init__(self, size=16):
        self.size = size

    # param text The padded text for which the padding is to be removed.
    # exception ValueError Raised when the input padding is missing or corrupt.
    def decode(self, text):
        '''
        Remove the PsizeCS#7 padding from a text string
        '''
        text_lenght = len(text)
        val = int(binascii.hexlify(text[-1]), 16)
        if val > self.size:
            raise ValueError('Input is not padded or padding is corrupt')

        diff_lenght = text_lenght - val
        return text[:diff_lenght]

    #param text The text to encode.
    def encode(self, text):
        '''
        Pad an input string according to PCS#7
        '''
        text_lenght = len(text)
        output = StringIO.StringIO()
        val = self.size - (text_lenght % self.size)
        for _ in xrange(val):
            output.write('%02x' % val)
        return text + binascii.unhexlify(output.getvalue())

     
