class ListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class SinglyLinkedListIterator:

    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        if firstNode:
            self.size = 1
        else:
            self.size = 0

    def addNode(self, data):  # attach or anexar um Node depois do iterador:

        newNode = ListNode(data, None)  # treats the empty list ; trata a lista vazia
        newNode.nextNode = None
        if (self.size == 0):  # treats the empty list ; trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:  # iterator is on the last element ; o iterador está no último elemento
            self.lastNode.nextNode = newNode  # este Noh para a ser agora o ultimo Noh
            self.iterator = newNode
            self.lastNode = newNode  # por o ponteiro lastNode sobre o ultimo Noh
        else:  # iterator is on an inner element ; o iterador está em algum elemento interno
            newNode.nextNode = self.iterator.nextNode  # novo Noh aponta para o noh seguinte do iterador
            self.iterator.nextNode = newNode  # faz o prox do no sob o iterador apontar para o novo no
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

    def insNode(self, data):  # insere um Node antes do iterador
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh antes do iterador. O iterador fica sobre este Noh.
        """
        newNode = ListNode(data, None)  # treats the empty list ; trata a lista vazia
        newNode.nextNode = None
        if (self.size == 0):  # treats the empty list ; trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.firstNode:  # iterator is on the first element ; o iterador está no primeiro elemento
            newNode.nextNode = self.firstNode  # o novo noh aponta para o antigo primeiro noh
            self.firstNode = newNode  # firstNode aponta para o novoNoh que passa a ser o primeiro noh
            self.iterator = newNode  # o iterador fica sob o novoNoh que foi inserido
        else:  # iterator is on an inner element ; o iterador está em algum elemento interno
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            newNode.nextNode = self.iterator  # novo Noh aponta para o noh onde esta o iterador
            currentNode.nextNode = newNode  # o campo nextNode do noh corrente aponta para o novo no
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

        # o nextNode do noh 4 vai apontar para o noh com o 5
        # self.iterator.antNode.nextNode = newNode
        # newNode.antNode = self.iterator.antNode
        # newNode.nextNode = self.iterator
        # self.iterator.antNode = newNode
        # self.iterator = newNode

    def elimNode(self):  # elimina o elemento que está sobre o iterador e avanca o iterador para proximo Noh.
        if (self.iterator == self.firstNode):  # iterador sobre o primeiro elemento
            if (self.lastNode == self.firstNode):  # tem so um Noh
                self.lastNode = None  # aponta para nada
                self.firstNode = None
                self.iterator = None
            else:  # tem mais de um Node
                # self.firstNode = self.firstNode.nextNode # firstNode aponta para o proximo noh que passa a ser o primeiro
                self.firstNode = self.firstNode.nextNode  # self.iterator.nextNode
                self.iterator.nextNode = None  # isola o Noh
                self.iterator = self.firstNode  # avanca para o proximo Noh
        else:  # iterator pode estar sob o ultimo ou um elemento interno
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            if self.iterator == self.lastNode:  # o iterador esta sob o ultimo:
                # por lastNode sob o penultimo elemento: percorrer a lista ate parar antes do iterador
                # para tal usar um ponteiro auxiliar currentNode
                self.lastNode = currentNode  # o penultimo(currentNode) agora passa a ser o ultimo Noh
                self.iterator.nextNode = None  # isola o Node
                self.iterator = None  # iterador fica indefinido
                currentNode.nextNode = None  # ultimo Node nao tem proximo
            else:  # iterador sobre elemento intermediario
                currentNode.nextNode = self.iterator.nextNode  # o noh anterior ao que sera eliminado aponta para o seguinte deste noh
                currentNode = self.iterator  # guarda o Noh que vai ser eliminado
                self.iterator = self.iterator.nextNode  # avanca o iterador para o proximo noh
                currentNode.nextNode = None  # isola o noh
        self.size = self.size - 1  # decrementa o tamanho da lista
        return True

    def first_Node(self):  # coloca o iterador sobre o primeiro Node da Lista
        self.iterator = self.firstNode
        return True

    def last_Node(self):  # coloca o iterador sobre o útlimo Node da Lista
        self.iterator = self.lastNode
        return True

    def nextNode(self):  # avança o iterador uma posição. para tal o iterador deve estar definido(sobre um Noh)
        if (self.iterator):
            self.iterator = self.iterator.nextNode
        return True

    # def antNode(self):

    def posNode(self, position):  # coloca o iterador sobre a posição position
        """o iterador eh posto sobre o Nod da posicao que vai de 1 ate size.
           qualquer outro valor leva o iterador a ficar indefinido(None)
           Return True para posicao valida e False para iterador indefinido
        """
        if (position > 0 and position <= self.size):
            i = 1
            self.iterator = self.firstNode  # poe o iterador sob o primeiro Node
            while (i < position):
                if (self.iterator.nextNode != None):
                    self.iterator = self.iterator.nextNode
                    i = i + 1
            return True
        else:
            return False

    def isUndefinedIterator(self):  # retorna verdadeiro se o iterador estiver indefinido
        if (self.iterator == None):
            return True
        else:
            return False

    def printNode(self):
        curr = self.firstNode
        while curr:
            print(curr.data)
            curr = curr.nextNode
