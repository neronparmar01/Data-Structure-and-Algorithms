# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```
In this function, its taking two parameters, the first one is value and another parameter is number. So, if the value of number is 0, then 1 is returned and if the value of the number is 1, then the value of parameter is returned. Otherwise, the function is called recursively with the value of parameter and the number-1 as the arguments and also the result is multiplied by the value parameter and returned.

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```
The above given function is a recusrsive function that is taking one parameter called mystring. However, this function checks if the first and the last characters of the strings are equal or not. If the characters of the string are not equal then the boolean value of false is returned and they are equal then the function is called recursively. The calling of function recursively will continue till the lenght of the string is either of the values that is 0 or 1.


### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```
The above given function is too a recursive function as of all the previous ones. Also in this function the two parameters are passed which are value and the number. In this if the value of the number is 0, then it will return 1 and if the the value of the number is 1, then it will return the value of the parameter. However, if none of these applies then the funstion will recursively call itself with the same value parameter and half the value of number as argument and store the resulting value. Moreover, if the value of number is even, then the result is its square and if odd value number, then it will multiply the result by the value of parameter and sqaure it before returning it.

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

While writing a recursive functions, i always start by identifying the base case and writing the code for it. Later, i define the recursive case in terms of calling the function.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 

The analyzing of the recursive function involves the looking at each recursive call and considering how the input changes with each level of recursion. The base case is usually the simplest case to analyze, since it involves no further recursion. The function then can be analyzed by considering how the inputs are modified with each recursive call. This is similar to analyzing non-recursive call, where i consider how inputs are transformed into outputs through series of steps. However, the main difference is that recursive functions repeat the same code with modified inputs, while non-recursive functions typically involve distinct steps that are executed once and discarded.
