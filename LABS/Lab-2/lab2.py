# copy over your code from lab 1 to this file

# code from the lab1 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b    

def sum_to_goal(number, goals):
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[i] + number[j] == goals:
                return number[i] * number[j]
    return 0
    