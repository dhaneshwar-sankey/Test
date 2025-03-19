# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()  # Output: 10 → 20 → 30 → None
