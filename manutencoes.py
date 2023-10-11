from ArrayQueue import ArrayQueue

class Manutencao:
    def __init__(self, nomeRodovia, dataManutencao):
        self.nomeRodovia = nomeRodovia
        self.dataManutencao = dataManutencao

class fila:
    def __init__(self):
        self._filaManutencao = ArrayQueue()

    def enfileirarManutencao(self, nomeRodovia, dataManutencao):
        manutencao = Manutencao(nomeRodovia,dataManutencao)
        self._filaManutencao.enqueue(manutencao)

    def desenfileirar(self):
        if self._filaManutencao.is_empty():
            print ("Não há manutenções")
            return None
        manutencao = self._filaManutencao.dequeue()
        return manutencao.nomeRodovia, manutencao.dataManutencao


queueMaintenance = fila()


queueMaintenance.enfileirarManutencao("BR-262", "20/07/2014")
queueMaintenance.enfileirarManutencao("BR-230", "17/07/2007")
queueMaintenance.enfileirarManutencao("BR-101", "29/03/2009")
queueMaintenance.enfileirarManutencao("BR-317", "13/09/2010")
queueMaintenance.enfileirarManutencao("BR-153", "22/05/2013")
queueMaintenance.enfileirarManutencao("BR-364", "10/08/2015")
queueMaintenance.enfileirarManutencao("BR-222", "14/10/2019")

nomeRodovia, dataManutencao = queueMaintenance.desenfileirar()
print ("Foi feita manutenção na rodovia", nomeRodovia, "na data", dataManutencao)