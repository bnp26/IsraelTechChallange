import os
import sys

def merge_sort(nums1, nums2):
    merged = []
    x = 0
    a = 0
    b = 0
    while x < len(nums1) + len(nums2):
	if nums1[a] <= nums2[b]:
	    merged.append(nums1[a])
	    a += 1
	else:
	    merged.append(nums2[b])
	    b += 1
	x+=1
    return merged

def get_nums(line):
    nums = []
    line_ending = ""
    if line[:len(line)-2] != '\r\n':
	line_ending = '\r\n'
    else:
	line_ending = '\n'
    while len(line) >=2:
	str_split = line.split("\t",1)
	nums.append(int(str_split[0]))
	if len(str_split) == 1:
	    break
	else:
	    line = str_split[1]
    return nums



def main(input_file, output_file):
    nums_file = open(input_file, 'r')
    out = open(output_file, 'w')
    
    nums1 = []
    nums2 = []
    lines = nums_file.readlines()
    x = 0
    while lines[x] != None:
	if x == 0:
	    nums1.append(get_nums(lines[x]))
	else:
	    nums2.append(get_nums(lines[x]))
    merged = merge_sort(nums1, nums2)
    nums_file.close()
    for x in range(0, len(merged)):
	if x < len(merged):
	    out.write(merged[x])
	    out.write('\t')
	else:
	    out.write(merged[x])
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
