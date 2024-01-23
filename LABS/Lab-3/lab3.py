#
# Author: Neron Parmar
# Student Number: 171690217
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)

def linear_search(list, key, index=0):
	if index == len(list):
		return -1
	elif list[index] == key:
		return index
	else:
		return linear_search(list, key, index+1)

def binary_search(list, key, start = 0, end = None):
	if end == None:
		end = len(list) - 1
	if start > end:
		return -1
	mid = (start + end) // 2
	if list[mid] == key:
		return mid
	elif key < list[mid]:
		return binary_search(list, key, start, mid-1)
	else:
		return binary_search(list, key, mid+1, end)