#Author: Benjamin Poreh
#ITC programming challange #1 

#I use python because it's very simple to implement solutions to coding challanges in general.
#Additionally, python allows for easy manipulation of data and a huge assortment of different datastructures to choose from.

#first implementing my own hash map without a data secondary array.
class HashMap:
    def __init__(self):
	#there are 256 ascii characters
	self.size = 256
	self.keys = [None] * self.size
    
    #implementing the put method (adding a value to the hash map
    def put(self, char):
	ascii_val=ord(char)
	
	if self.keys[ascii_val] == None:
	    self.keys[ascii_val] = ord(char)
	#if this doesn't go through, then we don't really care since we are only looking for the first index.
	#it didn't specify otherwise in the challange.

    def has(self, char):
	ascii_val=ord(char)
	if self.keys[ascii_val] == None:
	    return None
	else:
	    return True

#could not name the first param as str because it's a keyword in python
#could not name the second param as set because it's ALSO a keyword in python
def find_substring(__str__, __set__):
    ascii_map = HashMap()
    counter = 0
    for char in __set__:
	ascii_map.put(char)
    for char in __str__:
	if ascii_map.has(char) == True:
	    return counter
	else:
	    counter+=1

#to test the function run the following (it will print out the answer for you
def main(str1, str2):
    print "str = " + str1
    print "set = " + str2
    print "answer = " + repr(find_substring(str1, str2))
    
if __name__ == '__main__':
	main("IsraelTechChallange", "hlartT")
