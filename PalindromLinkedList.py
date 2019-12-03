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

    def printLL(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end="->")
            tmp = tmp.next
        print(None)

    def clone(self):
        ll = LinkedList()
        tmp = self.head
        while tmp.next is not None:
            ll.push(tmp.data)
            tmp = tmp.next
        ll.push(tmp.data)
        return ll

    # checking via reversing
    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while current:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    def isEqual(self, ll2):
        a = self.head
        b = ll2.head
        while a and b:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return True


ll1 = LinkedList()
# ll2 = LinkedList()
ll1.push(1)
ll1.push(2)
ll1.push(3)
ll1.push(2)
ll1.push(1)

print("Given linked list is:")
ll1.printLL()
print("Reversed linked list is:")
ll2 = ll1.clone()
ll2.printLL()
# print("Original linked list is:")
# ll1.printLL()
print("Is the given linkedlist a palindrome: ", end='')
print(ll1.isEqual(ll2))

