# Name : Neron Parmar
# Student ID : 171690217
# Date : 10/10/2023
# All the work of the assignment is done by my own and no file of mine and no part of my file has been shared with anyone.

import random

# Counter for tracking the number of steps
def bubble_sort(my_list):
    n = len(my_list)
    steps = 0  # Initialize the counter
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1  # Increment the counter for each comparison
            if my_list[j] > my_list[j+1]:
                steps += 3  # Increment the counter for the swap (3 steps)
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list, steps  # Return the sorted list and the total number of steps

def selection_sort(my_list):
    n = len(my_list)
    steps = 0  # Initialize the counter
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps += 1  # Increment the counter for each comparison
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        steps += 3  # Increment the counter for the swap (3 steps)
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list, steps  # Return the sorted list and the total number of steps

def insertion_sort(my_list):
    n = len(my_list)
    steps = 0  # Initialize the counter
    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            steps += 2  # Increment the counter for each comparison and shift
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
    return my_list, steps  # Return the sorted list and the total number of steps

def quick_sort(my_list):
    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            right = [x for x in arr[1:] if x > pivot]
            sorted_left, left_steps = _quick_sort(left)
            sorted_right, right_steps = _quick_sort(right)
            steps = left_steps + right_steps + len(arr) - 1  # Count comparisons in this step
            return sorted_left + [pivot] + sorted_right, steps

    sorted_list, steps = _quick_sort(my_list)
    return sorted_list, steps  # Return the sorted list and the total number of steps

def insertion_sort_with_indices(my_list, left, right):
    steps = 0  # Initialize the counter
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        while j >= left and key < my_list[j]:
            steps += 2  # Increment the counter for each comparison and shift
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list, steps  # Return the sorted list and the total number of steps

def main():
    my_list = [random.randint(0, 100) for _ in range(100)]

    # Best-case scenario (sorted list)
    best_case_list = list(range(100))

    # Worst-case scenario (reverse sorted list)
    worst_case_list = list(range(100, 0, -1))

    # Average-case scenario (random list)
    average_case_list = [random.randint(0, 100) for _ in range(100)]

    scenarios = [
        ("Best Case (Sorted List)", best_case_list),
        ("Worst Case (Reverse Sorted List)", worst_case_list),
        ("Average Case (Random List)", average_case_list)
    ]

    for scenario_name, scenario_list in scenarios:
        print(f"Scenario: {scenario_name}")
        print("Original List:", scenario_list)

        # Testing and measuring steps for each scenario
        bubble_sorted, bubble_steps = bubble_sort(scenario_list.copy())
        selection_sorted, selection_steps = selection_sort(scenario_list.copy())
        insertion_sorted, insertion_steps = insertion_sort(scenario_list.copy())
        quick_sorted, quick_steps = quick_sort(scenario_list.copy())
        insertion_with_indices_sorted, insertion_with_indices_steps = insertion_sort_with_indices(scenario_list.copy(), 0, len(scenario_list) - 1)

        # Printing results
        print("\nBubble Sort:")
        print("Sorted List:", bubble_sorted)
        print("Number of steps:", bubble_steps)

        print("\nSelection Sort:")
        print("Sorted List:", selection_sorted)
        print("Number of steps:", selection_steps)

        print("\nInsertion Sort:")
        print("Sorted List:", insertion_sorted)
        print("Number of steps:", insertion_steps)

        print("\nQuick Sort:")
        print("Sorted List:", quick_sorted)
        print("Number of steps:", quick_steps)

        print("\nInsertion Sort with Indices:")
        print("Sorted List:", insertion_with_indices_sorted)
        print("Number of steps:", insertion_with_indices_steps)

        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
