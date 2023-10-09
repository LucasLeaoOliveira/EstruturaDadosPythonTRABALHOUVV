from cidade import Cidade
from listaSimplesmenteEncadeada import SinglyLinkedListIterator


class Rodovia:
    def __init__(self, nome):
        self.nome = nome
        self.primeira_cidade = None  # Atributo para a primeira cidade da rodovia

    def adicionar_cidade(self, nome_cidade):
        nova_cidade = Cidade(nome_cidade)
        if self.primeira_cidade is None:
            self.primeira_cidade = nova_cidade
        else:
            # Encontrar a última cidade na lista e definir sua próxima cidade
            cidade_atual = self.primeira_cidade
            while cidade_atual.proxima_cidade is not None:
                cidade_atual = cidade_atual.proxima_cidade
            cidade_atual.proxima_cidade = nova_cidade

    def listar_cidades(self):
        cidades = []
        cidade_atual = self.primeira_cidade
        while cidade_atual is not None:
            cidades.append(cidade_atual.nome)
            cidade_atual = cidade_atual.proxima_cidade
        return cidades


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

if __name__ == "__main__":
    # Criando uma rodovia
    br_101 = Rodovia("BR-101")
    br_101.adicionar_cidade("Criciuma")
    br_101.adicionar_cidade("Floripa")
    br_101.adicionar_cidade("Sombrio")

    # Listando cidades na rodovia
    print("Cidades na BR-101:", br_101.listar_cidades())

    # Adicionando mais cidades
    br_101.adicionar_cidade("Porto Alegre")
    br_101.adicionar_cidade("Curitiba")

    # Listando cidades novamente
    print("Cidades na BR-101 após adição de mais cidades:", br_101.listar_cidades())
