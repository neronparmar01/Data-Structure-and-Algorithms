# Name : Neron Parmar
# Student ID : 171690217
# Date : 10/10/2023
# All the work of the assignment is done by my own and no file of mine and no part of my file has been shared with anyone.

import random
import time

# Bubble Sort with step count
def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1  # Counting the comparison
            if my_list[j] > my_list[j+1]:
                steps += 4  # Counting 3 steps for the swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return steps

# Selection Sort with step count
def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps += 1  # Counting the comparison
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
        steps += 3  # Counting 3 steps for the swap
    return steps

# Insertion Sort with step count
def insertion_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            steps += 2  # Counting 2 steps: comparison and shifting
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
        steps += 1  # Counting the last assignment
    return steps

# Quick Sort with step count (iterative)
def quick_sort(my_list):
    steps = 0
    stack = [(0, len(my_list) - 1)]

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = my_list[right]
            i = left - 1
            for j in range(left, right):
                steps += 1  # Counting the comparison
                if my_list[j] <= pivot:
                    i += 1
                    my_list[i], my_list[j] = my_list[j], my_list[i]
                    steps += 3  # Counting 3 steps for the swap
            my_list[i+1], my_list[right] = my_list[right], my_list[i+1]
            steps += 3  # Counting 3 steps for the swap

            stack.append((left, i))
            stack.append((i + 2, right))

    return steps

# Insertion Sort with step count and left/right indices
def insertion_sort_with_indices(my_list, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        while j >= left and key < my_list[j]:
            steps += 2  # Counting 2 steps: comparison and shifting
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
        steps += 1  # Counting the last assignment
    return steps


# Main function for Step 4
def main():
    list_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]

    for size in list_sizes:
        rand_list = [random.randint(0, 100) for _ in range(size)]
        print(f"List size: {size}")

        # Bubble Sort
        bubble_copy = rand_list.copy()
        start_time = time.time()
        bubble_steps = bubble_sort(bubble_copy)
        end_time = time.time()
        print(f"Bubble Sort Steps: {bubble_steps}, Time: {end_time - start_time:.6f} seconds")

        # Selection Sort
        selection_copy = rand_list.copy()
        start_time = time.time()
        selection_steps = selection_sort(selection_copy)
        end_time = time.time()
        print(f"Selection Sort Steps: {selection_steps}, Time: {end_time - start_time:.6f} seconds")

        # Insertion Sort
        insertion_copy = rand_list.copy()
        start_time = time.time()
        insertion_steps = insertion_sort(insertion_copy)
        end_time = time.time()
        print(f"Insertion Sort Steps: {insertion_steps}, Time: {end_time - start_time:.6f} seconds")

        # Insertion Sort with Indices
        insertion_indices_copy = rand_list.copy()
        start_time = time.time()
        insertion_indices_steps = insertion_sort_with_indices(insertion_indices_copy, 0, len(insertion_indices_copy) - 1)
        end_time = time.time()
        print(f"Insertion Sort with Indices Steps: {insertion_indices_steps}, Time: {end_time - start_time:.6f} seconds")

        # Quick Sort
        quick_copy = rand_list.copy()
        start_time = time.time()
        quick_steps = quick_sort(quick_copy)
        end_time = time.time()
        print(f"Quick Sort Steps: {quick_steps}, Time: {end_time - start_time:.6f} seconds")

        print("----------------------")

if __name__ == "__main__":
    main()
