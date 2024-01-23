# Name : Neron Parmar
# Student ID : 171690217
# Date : 10/10/2023
# All the work of the assignment is done by my own and no file of mine and no part of my file has been shared with anyone.

# bubble sort function
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
 
# selection sort function
def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list
 
# insertion sort function
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i-1
        while j >=0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
    return my_list
 
# quick sort function
def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        pivot = my_list[0]
        left = []
        right = []
        for x in my_list[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)
 
# insertion sort function with range
def insertion_sort_range(my_list, left, right):
    for i in range(left+1, right+1):
        key = my_list[i]
        j = i-1
        while j >= left and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key
    return my_list
 
# main function to test the above functions
def main():
    import random
    
    # generate a list of length 100 with random integers
    my_list = [random.randint(0,100) for i in range(100)]
    
    # test each sorting function
    print("Unsorted list:")
    print(my_list)
    print("Bubble sorted list:")
    print(bubble_sort(my_list))
    print("Selection sorted list:")
    print(selection_sort(my_list))
    print("Insertion sorted list:")
    print(insertion_sort(my_list))
    print("Quick sorted list:")
    print(quick_sort(my_list))
    print("Insertion sorted list with range:")
    print(insertion_sort_range(my_list, 0, len(my_list)-1))
    
if __name__ == "__main__":
    main()