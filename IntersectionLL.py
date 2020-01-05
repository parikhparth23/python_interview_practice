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

    def intersection(self, head1, head2):
        len1 = 0
        len2 = 0
        cur1 = head1
        cur2 = head2

        while head1 is not None:
            len1 += 1
            cur1 = cur1.next

        while head2 is not None:
            len2 += 1
            cur2 = cur2.next

        cur1 = head1
        cur2 = head2

        if len1 > len2:
            for i in range(len1 - len2):
                cur1 = cur1.next
        elif len2 > len1:
            for i in range(len2 - len1):
                cur2 = cur2.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1


ll1 = LinkedList()
ll1.push(1)
ll1.push(2)
ll1.push(7)
ll1.push(9)
ll1.push(5)
ll1.push(1)
ll1.push(3)
print("ll1 is: ")
ll1.printLL()

ll2 = LinkedList()
ll2.push(1)
ll2.push(2)
ll2.push(7)
ll2.push(6)
ll2.push(4)
print("ll2 is: ")
ll2.printLL()

print("Intesection of ll is:")
print(intersection(ll1, ll2))