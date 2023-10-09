class ListNode:
    def __init__(self, data, prevNode=None, nextNode=None):
        self.data = data
        self.prevNode = prevNode
        self.nextNode = nextNode


class DoublyLinkedList:
    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode

    def addNode(self, data):  # adiciona Node depois do iterador e it fica neste Node
        new_node = ListNode(data, self.iterator, self.iterator.nextNode)
        if self.iterator.nextNode:
            self.iterator.nextNode.prevNode = new_node
        self.iterator.nextNode = new_node
        self.iterator = new_node
        if new_node.nextNode is None:
            self.lastNode = new_node

    def insNode(self, data):  # insere Node antes do iterador e it fica neste Node
        new_node = ListNode(data, self.iterator.prevNode, self.iterator)
        if self.iterator.prevNode:
            self.iterator.prevNode.nextNode = new_node
        self.iterator.prevNode = new_node
        self.iterator = new_node
        if new_node.prevNode is None:
            self.firstNode = new_node

    def elimNode(self):  # elimina Node sob it e it avança p/ próximo Node
        if self.iterator:
            if self.iterator.prevNode:
                self.iterator.prevNode.nextNode = self.iterator.nextNode
            if self.iterator.nextNode:
                self.iterator.nextNode.prevNode = self.iterator.prevNode
            self.iterator = self.iterator.nextNode

    def first_Node(self):  # coloca o iterador sobre o primeiro Node da Lista
        self.iterator = self.firstNode

    def last_Node(self):  # coloca o iterador sobre o último Node da Lista
        self.iterator = self.lastNode

    def nextNode(self):  # avança it uma posição. Se it no último Node, it=None
        if self.iterator:
            self.iterator = self.iterator.nextNode

    def anttNode(self):  # retrocede it uma posição. Se it no primeiro Node, it=None
        if self.iterator:
            self.iterator = self.iterator.prevNode

    def posNode(self, position):  # põe it em <=1 pos <=size, senão it=None
        current_pos = 1
        current_node = self.firstNode
        while current_node and current_pos < position:
            current_node = current_node.nextNode
            current_pos += 1
        self.iterator = current_node

    def undefinedIterator(self):  # True se o it=None e False o contrário
        return self.iterator is None
