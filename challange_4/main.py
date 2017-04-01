import sys, getopt

def num_of_bits(integer):
    binary = str(bin(integer)[2:])
    counter = 0
    for x in binary:
        if x == '1':
            counter = counter + 1
    return counter
    
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
        nums.append(int(number))
    
    nums_file.close()
    
    out.truncate()

    num_bits = []
    for number in nums:
        num_bits.append(num_of_bits(number))
    
    for n in num_bits:
        out.write(str(n))
        out.write('\r\n')
    
if __name__ == "__main__":
    input_file = ''
    output_file = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input_file = arg
      elif opt in ("-o", "--ofile"):
         output_file = arg
    main()
