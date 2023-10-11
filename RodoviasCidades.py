from SinglyLinkedListIterator import *

class ListNode:
    def __init__(self, data, prevNode=None, nextNode=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, firstNode=None):
        self.first = None
        self.prev = None

    def addNode(self, data):
        new_node = ListNode(data)
        if self.first is None:
            self.first = new_node
            self.prev = new_node
        else:
            new_node.prev = self.prev
            self.prev.next = new_node
            self.prev = new_node

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.next

class Rodovia:
    def __init__(self, nome):
        self.nome = nome
        self.cidades = DoublyLinkedList()

    def adicionar_cidade(self, cidade):
        self.cidades.addNode(cidade)

    @staticmethod
    def ler_arquivo(nome_do_arquivo):
        rodovias = []
        with open(nome_do_arquivo, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split()
                nome_rodovia = dados[0]
                cidades = dados[1:]
                rodovia = Rodovia(nome_rodovia)
                for cidade in cidades:
                    rodovia.adicionar_cidade(cidade)
                rodovias.append(rodovia)
        return rodovias


def rodoviasCidade(nomeCidade, lstRodovias):
    rodovias_que_passam = DoublyLinkedList()

    for rodovia in lstRodovias:
        for cidade in rodovia.cidades:
            # Use strip() para remover espaços extras e lower() para comparar em minúsculas
            if cidade.strip().lower() == nomeCidade.strip().lower():
                rodovias_que_passam.addNode(rodovia.nome)

    return rodovias_que_passam

# Uso das funções na classe Rodovia
rodovias = Rodovia.ler_arquivo('arquivo.txt')
cidade_desejada = "Vix"
rodovias_que_passam_por_cidade = rodoviasCidade(cidade_desejada, rodovias)

for rodovia in rodovias_que_passam_por_cidade:
    print(rodovia)