#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Usage Example -
python steganography.py -f X.bmp -o Y.bmp -m "Hidden message!"
'''



from optparse import OptionParser


__author__ = "ITC"
__license__ = "GPLv3"

from PIL import Image
import binascii
from bitstring import BitArray

try:
   input = raw_input
except NameError:
   pass

def reset_bit(v, index):
  """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
  mask =  v >> index
: print mask
  return mask%2

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    message = ''
    word = ''
    
    while len(bits) > 8:
	word_list = bits[0:8]
	print str(word_list)
	for x in word_list:
	    word += str(x)
	bits = bits[8:]
	
	b = BitArray(bin=word)
	print b.uint
	if b.uint > 127:
	    break
	message += str(unichr(b.uint))
	word = ''
	    
    return message
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def setlsb(component, bit):
    """
    Set Least Significant Bit of a colour component.
    """
    return component & ~1 | int(bit)

def a2bits_list(chars):
    """
    Convert a string to its bits representation as a list of 0's and 1's.
    """
    return [bin(ord(x))[2:].rjust(8,"0") for x in chars]

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def reveal(input_image_file, auto_convert_rgb=False, order_func = fib):
    
    #opening the inputed image.
    img = Image.open(input_image_file)
    hidden_bits_order = order_func()
    decoded = img.copy()
    width, height = img.size

    index = 0
    message_bits = []
    for row in range(height):
	for col in range(width):
	    pixel = img.getpixel((col, row))
	    r = pixel[0]
	    g = pixel[1]
	    b = pixel[2]
	    bit = hidden_bits_order.next() % 8
	    bit_r = reset_bit(r, bit)
	    bit_g = reset_bit(g, bit)
	    bit_b = reset_bit(b, bit)
	    message_bits.append(bit_r)
	    message_bits.append(bit_g)
	    message_bits.append(bit_b)
	    index+=1
	    if index == 8*11:
		break
	if index == 8*11:
	    break

    print message_bits
    answer = text_from_bits(message_bits)
    img.close()
    print answer
    return answer

def main():

    # Read the imahe from disk
    encoded = reveal(options.input_file, True)
    target = open("log.txt", 'w') 
    target.write("file")
    target.write(encoded)
    target.close()

if __name__ == "__main__" :
    parser = OptionParser()
    parser.add_option("-f", "--input-file", dest="input_file",
                      help="input image file", action="store", type="string")

    (options, args) = parser.parse_args()

    if options.input_file == None:  # if filename is not given
        parser.error('all parameters are required')

    main()
