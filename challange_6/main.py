import os

def merge_sort(nums1, nums2):
    merged = []
    x = 0
    c1 = 0
    c2 = 0
    while x < len(nums1) + len(nums2):
	if nums1

def main(input_file, output_file):
    nums_file = open(input_file, 'r')
    out = open(output_file, 'w')
    
    nums = []
    lines = nums_file.readlines()
    for line in lines:
	line_ending = ""
	if line[:len(line)-2] != '\r\n':
	    line_ending = '\r\n'
	else:
	    line_ending = '\n'
        while line != line_ending:
            str_split = line.split("\t",1)
	    nums.append(int(str_split[0]))
	    if len(str_split) == 1:
		break
	    else:
		line = str_split[1]
    nums_file.close() 

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
