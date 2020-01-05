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
        while tmp is not None:
            print(tmp.data, end="->")
            tmp = tmp.next
        print(None)

    def deleteNode(self, key):
        tmp = self.head

        # if its the first node to be deleted
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                return

        tmp = self.head
        if tmp.next is None:
            tmp = tmp.next
        if tmp.data == key:
            return

        # if key is between the first and the last
        tmp = self.head
        prev = None
        while tmp is not None:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp is None:
            return

        prev.next = tmp.next


ll = LinkedList()
ll.push(9)
ll.push(1)
ll.push(5)
ll.push(4)
print("Original LinkedList:")
ll.print()
print("LinkedList after deleting a Node")
ll.deleteNode(9)
ll.print()
