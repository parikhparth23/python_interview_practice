class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def newNode(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.next = None
        return new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def partition(self, x):
        tail = self.head

        current = self.head
        while current is not None:
            next = current.next
            if(current.data < x):
                current.next = self.head
                tail = current
            else:
                tail.next = current
                tail = current

            current = next
        tail.next = None

        # return head

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end='->')
            tmp = tmp.next
        print(None)


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(10)
ll.push(5)
ll.push(8)
ll.push(5)
ll.push(3)

x = 5

print("LinkedList:")
ll.print()
print("LinkedList after partiotion:")
ll.partition(x)
ll.print()
