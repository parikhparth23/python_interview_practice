class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end="->")
            tmp = tmp.next
        print(None)

    def reverse_ll(self):
        prev = None
        current = self.head

        while current:
             next = current.next
             current.next = prev
             prev = current
             current = next
        self.head =  prev

ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)

print("Given linked list is:")
ll.print()

print("Reverse linked list is:")
ll.reverse_ll()
ll.print()



