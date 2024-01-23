# Name : Neron Parmar
# Student ID : 171690217
# Date : 10/10/2023
# All the work of the assignment is done by my own and no file of mine and no part of my file has been shared with anyone.

import matplotlib.pyplot as plt
import sys

# increase recursion depth to prevent maximum recursion error
sys.setrecursionlimit(10 ** 6)


# updated bubble sort function with T(n) calculation
def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            steps += 1  # comparison operation
            if my_list[j] > my_list[j + 1]:
                steps += 4  # swap operation
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list, steps


def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1  # comparison operation
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        steps += 1  # swap operation
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list, steps


# updated insertion sort function with T(n) calculation
def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            t += 2  # comparison + shift operation
            my_list[j + 1] = my_list[j]
            j -= 1
        steps += 1  # swap operation
        my_list[j + 1] = key
    return my_list, steps


# updated quick sort function with T(n) calculation
def quick_sort(my_list):
    steps = 0
    if len(my_list) <= 1:
        return my_list, steps
    else:
        pivot = my_list[0]
        left = []
        right = []
        for x in my_list[1:]:
            steps += 1  # comparison operation
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        sub_steps = 0
        sub_left, sub_steps_l = quick_sort(left)
        sub_right, sub_steps_r = quick_sort(right)
        steps += sub_steps + sub_steps_l + sub_steps_r
        return sub_left + [pivot] + sub_right, steps


# updated insertion sort function with range and T(n) calculation
def insertion_sort_range(my_list, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        while j >= left and key < my_list[j]:
            t += 2  # comparison + shift operation
            my_list[j + 1] = my_list[j]
            j -= 1
        steps += 1  # swap operation
        my_list[j + 1] = key
    return my_list, steps


# plotting T(n) vs. n for various list sizes using worst case scenario
def plot_tn_vs_n():
    list_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]
    t_values = []

    for size in list_sizes:
        rand_list_worst = list(range(size, 0, -1))  # Worst-case scenario
        steps = bubble_sort(rand_list_worst)  # Choose the sorting function to test
        steps = selection_sort(rand_list_worst)
        steps = insertion_sort(rand_list_worst)
        steps = quick_sort(rand_list_worst)
        steps = insertion_sort_range(rand_list_worst)
        steps_values.append(steps[1])

    plt.plot(list_sizes, steps_values)
    plt.xlabel('List Size (n)')
    plt.ylabel('T(n)')
    plt.title('T(n) vs. n for Bubble Sort (Worst Case)')
    n_values = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]
    plt.show()

    bubble_sort_t = []
    selection_sort_t = []
    insertion_sort_t = []
    quick_sort_t = []
    insertion_sort_range_t = []

    for n in n_values:
        lst = list(range(n, 0, -1))
        bubble_sort_t.append(bubble_sort(lst)[1])
        selection_sort_t.append(selection_sort(lst)[1])
        insertion_sort_t.append(insertion_sort(lst)[1])
        quick_sort_t.append(quick_sort(lst)[1])
        insertion_sort_range_t.append(insertion_sort_range(lst, 0, n - 1)[1])

    plt.plot(n_values, bubble_sort_t, label='Bubble Sort')
    plt.plot(n_values, selection_sort_t, label='Selection Sort')
    plt.plot(n_values, insertion_sort_t, label='Insertion Sort')
    plt.plot(n_values, quick_sort_t, label='Quick Sort')
    plt.plot(n_values, insertion_sort_range_t, label='Insertion Sort with Range')


plt.xlabel('n (List Size)')
plt.ylabel('T(n) (Number of steps)')
plt.title('T(n) vs. n for Various Sorting Algorithms (Worst Case)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

# # call the plot function
plot_tn_vs_n()
