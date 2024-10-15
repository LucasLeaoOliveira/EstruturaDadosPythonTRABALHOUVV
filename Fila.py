from ArrayQueue import ArrayQueue
from Manutencao import Manutencao

class Fila:
    def __init__(self):
        self._filaManutencao = ArrayQueue()

    def enfileirarManutencao(self, nomeRodovia, dataManutencao):
        manutencao = Manutencao(nomeRodovia, dataManutencao)
        self._filaManutencao.enqueue(manutencao)

    def desenfileirar(self):
        if self._filaManutencao.is_empty():
            print("Não há manutenções")
            return None
        manutencao = self._filaManutencao.dequeue()
        return manutencao.rodovia, manutencao.data  # corrigido para usar 'rodovia' e 'data'
