class Node:
    def __init__(self, data):
        self.data = data
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

    def removeNNode(self, key):
        length = 0
        tmp = self.head

        while tmp:
            length += 1
            tmp = tmp.next

        remove = length - key
        tmp = self.head
        for i in range(0, remove):
            prev = tmp
            tmp = tmp.next

        prev.next = tmp.next


ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print("Original LinkedList:")
ll.print()
print("LinkedList after deleting a Node")
ll.removeNNode(2)
ll.print()
