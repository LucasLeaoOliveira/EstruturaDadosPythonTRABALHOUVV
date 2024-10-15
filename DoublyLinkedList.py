class ListNode:
    def __init__(self, data, prevNode=None, nextNode=None):
        self.data = data
        self.prev = prevNode
        self.next = nextNode

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def addNode(self, data):
        new_node = ListNode(data)
        if self.first is None:  # If the list is empty
            self.first = new_node
            self.last = new_node
        else:  # Add at the end of the list
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.next
