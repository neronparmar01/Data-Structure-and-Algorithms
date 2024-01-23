# Assignment 2
# Name: Neron Parmar
# Student ID: 171690217
# File: a1.py
# Date: 11/3/23
# All the work in the assignment is done by my own and no part of my assigment is shared with anyone.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublySortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        # Complete this function
        
        # creating a node with the given data
        new_node = Node(data)
        
        # The base case List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current and current.data < data:
                current = current.next

            if current is None:
                # Insert at the end
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            elif current.prev is None:
                # Insert at the beginning
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                # Insert in the middle
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node

    def remove(self, data):
        # Complete this function
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True

            current = current.next
        return False

    def is_present(self, data):
        # Complete this function
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        # Complete this function
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        # Complete this function
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    # Write a main program that initiates the sorted linked lists and
    # uses the above methods so that you can test your code (Won't be marked)
    linked_list = DoublySortedLinkedList()

    # inserting the values into the list
    values = [5, 3, 8, 2, 6]
    for value in values:
        linked_list.insert(value)

    # displaying the list
    linked_list.display()

    # testing the methods
    print("Length of the list:", len(linked_list))
    print("Is element 3 present in the list?", linked_list.is_present(3))
    print("Is element 7 present in the list?", linked_list.is_present(7))
    
    # testing the remove method
    print("Remove element 2 that has value as 3 from the list:", linked_list.remove(2))
    
    # rechecking the list to confirm the remove method worked correctly or not
    print("Is element 2 having value as 3 present in the list?", linked_list.is_present(2))


if __name__ == '__main__':
    main()
