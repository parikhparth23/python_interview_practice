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
        while tmp is not None:
            print(tmp.data, end='->')
            tmp = tmp.next
        print(None)

    def removeMiddleElement(self):
        fast_ptr = self.head
        slow_ptr = self.head
        prev = None

        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            # old=prev
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            # print("prev ", prev.data)
            # print("slw_ptr ", slow_ptr.data)

        prev.next = slow_ptr.next
        # prev = old
        # prev.next = slow_ptr


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
print("LinkedList:")
ll.print()
ll.removeMiddleElement()
print("LinkedList after removing the middle element:")
ll.print()

