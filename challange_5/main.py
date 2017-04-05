'''
Author: Benjamin Poreh
email: bnp26@case.edu
hack.israeltechchallange account: bporeh
Data Structures Coding Challenge
'''

import sys

class Node(object):
    def __init__(self, value):
        self.value = value

class Stack(object):
    def __init__(self):
        self.node_stack = []
        self.mins_list = []
    def __min__(self):
        if len(self.mins_list) == 0:
            return None
        return self.mins_list[len(self.mins_list)-1]
    
    def push(self, value):
        node = Node(value)
        if len(self.node_stack) == 0:
            self.node_stack.append(node)
	    self.mins_list.append(node)
        else:
            minimum = self.__min__()
            if node.value <= minimum.value:
	        self.mins_list.append(node)
                self.node_stack.append(node)
        
    def pop(self):
        if len(self.node_stack) == 0:
            return None
        if self.node_stack[len(self.node_stack)-1] is self.__min__(self):
            self.mins_list.pop()
        
        return self.node_stack.pop().value()

    def min(self):
        if len(self.node_stack) == 0:
            return None
        return self.__min__().value

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
    stack = Stack()
    for num in nums:
        stack.push(num)

    out.write(str(stack.min()))
    out.write('\r\n')
    out.close()
    return
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
