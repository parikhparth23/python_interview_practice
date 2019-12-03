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

    # checking via reversing
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


def isEqual(ll1, ll2):
    while ll1 and ll2:
        if ll1.data != ll2.data:
            return False
        ll1 = ll1.next
        ll2 = ll2.next


ll1 = LinkedList()
ll2 = LinkedList()
ll1.push(1)
ll1.push(2)
ll1.push(3)
ll1.push(2)
ll1.push(1)

print("Given linked list is:")
ll1.print()
ll2 = ll1
print("Reversed linked list is:")
ll2.reverse()
ll2.print()

print(isEqual(ll1, ll2))
