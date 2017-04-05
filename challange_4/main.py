'''
Author: Benjamin Poreh
email: bnp26@case.edu
hack.israeltechchallange account: bporeh
'''

import sys

def num_of_bits(integer, counter):
	binary = str(bin(integer)[2:])
	current_bit = len(binary)-1
	counter+=1
	integer = integer - 2**current_bit
	if integer == 0:
		return counter
	else:
		return num_of_bits(integer, counter)

def main(input_file, output_file):
    '''
    if len(inputs) != 2:
        print "Incorrect format. \nShould be in the following format:\n python main.py [input_file] [output_file_name]"
        return
    '''
    nums_file = open(input_file, 'r')
    out = open(output_file, 'w')
    
    nums = []
    lines = nums_file.readlines()
    for line in lines:
        x = 0
        number =''
     
        while line[x:x+1].isdigit():
            number += line[x]
            x+=1

	if(number != ''):
	    nums.append(int(number))
    
    nums_file.close()
    out.truncate()
    counter = 0
    for x in nums:
        num_bits = num_of_bits(x, counter)  
        out.write(str(num_bits))
        out.write('\r\n')
    out.close()
    
if __name__ == "__main__":
    input_file = ''
    output_file = ''
    args = sys.argv
    num_args = len(sys.argv)
    if num_args != 3:
        print 'main.py <inputfile> <outputfile>'
        sys.exit(2)
    input_file = args[1]
    output_file = args[2]
    main(input_file, output_file)
