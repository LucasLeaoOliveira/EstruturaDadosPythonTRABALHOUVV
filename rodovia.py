from listaSimplesmenteEncadeada import SinglyLinkedListIterator


class Rodovia:
    def __init__(self, nome, cidades=None):
        self.nome = nome
        self.cidades = cidades


def rodoviasCidade(nomeCidade, lstRodovias):
    rodovias_que_passam_pela_cidade = SinglyLinkedListIterator()  # Lista encadeada para armazenar as rodovias

    current_node = lstRodovias.firstNode
    while current_node:
        rodovia = current_node.data
        if rodovia.cidades is not None and nomeCidade in rodovia.cidades:
            # Adiciona a rodovia à lista de rodovias que passam pela cidade
            rodovias_que_passam_pela_cidade.addNode(rodovia.nome)
        current_node = current_node.nextNode

    return rodovias_que_passam_pela_cidade

# Função para ler o arquivo de entrada e criar a estrutura de dados
def ler_arquivo_entrada(nome_arquivo):
    rodovias = SinglyLinkedListIterator()  # Lista encadeada para armazenar as rodovias

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Divide a linha em nome da rodovia e lista de cidades
                dados = linha.strip().split(' ')
                nome_rodovia = dados[0]
                cidades = dados[1:]

                # Cria um objeto Rodovia e adiciona à lista encadeada
                rodovia = Rodovia(nome_rodovia, cidades)
                rodovias.addNode(rodovia)

        return rodovias
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
        return None

# Exemplo de uso
nome_arquivo = 'entrada.txt'  # Nome do arquivo de entrada
lista_rodovias = ler_arquivo_entrada(nome_arquivo)

# Verifica se a lista de rodovias foi criada com sucesso
if lista_rodovias:
    print("Estrutura de dados populada a partir do arquivo de entrada:")
    lista_rodovias.printNode()  # Exibe as rodovias e suas cidades

