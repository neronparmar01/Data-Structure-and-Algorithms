# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;

	for i in range(0,number):
		x = (i+1)
		total+=(x*x)

	return total
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1 to number):
		total=total*(i+1)
	return total
```


## In class portion


### Group members
List the members of your group member below:

	* Name 	: Neron Parmar
	* Student Id : 171690217

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Neron Parmar |  4.418s | 0.645s |
| Neron Parmar |  3.827s | 0.617s |   


### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 0.617s | 0.645s | 0.028s |
|fibonacci | 3.827s | 4.418s | 0.591s |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

If seeing on the differences in the code there are few things that i found are as follows:
Seeing in the function 1, I didn't handled my case sensitivity well. Moreover, there was notable difference in syntax. However, there wasn't much difference seen. However, all these function focuses on the mathematical calculation and sorting, while for the code of lab1 there several specific function had specific approach for dealing such as mathematical calculation and game logic and so on.


## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

The differences between the fastest and the slowest version mainly depends on the algotrithms used in it. However, there wasn't seen much difference in the code, yet for the fibonacci series there was a 1 seconds difference obeserved.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?

The functions do not have significant memory overhead and apart from these they mostly use variables and don't create large data  structures. Thus, there are no large amount of spaces used.

3. What sort of conclusions can you draw based on your observations?

As per the observation i made, i just found that recursive algorithms tend to perform more slower than those of iterative ones. Therefore, it depends on the approach of the person that how effecient he/she writes down the code that optimizes both speed and memory usage.