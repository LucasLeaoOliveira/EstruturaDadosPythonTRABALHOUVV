from DoublyLinkedList import DoublyLinkedList

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
            if cidade.strip().lower() == nomeCidade.strip().lower():
                rodovias_que_passam.addNode(rodovia.nome)

    return rodovias_que_passam
