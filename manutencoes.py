from ArrayQueue import ArrayQueue

class Manutenção:
    def init(self, nomeRodovia, dataManutenção):
        self.nomeRodovia = nomeRodovia
        self.dataManutencao = dataManutenção

class fila:
    def init(self):
        self._filaManutenção = ArrayQueue()

    def enfileirarManutenção(self, nomeRodovia, dataManutenção):
        manutenção = Manutenção(nomeRodovia,dataManutenção)
        self._filaManutenção.enqueue(manutenção)

    def desenfileirar(self):
        if self._filaManutenção.is_empty():
            print ("Não há manutenções")
            return None
        manutenção = self._filaManutenção.dequeue()
        return manutenção.nomeRodovia, manutenção.dataManutenção


queueMaintenance = fila()

queueMaintenance.enfileirarManutenção ("BR-101", "22/08/2003")
queueMaintenance.enfileirarManutenção ("BR-262", "20/07/2014")
queueMaintenance.enfileirarManutenção ("BR-230", "17/07/2007")
queueMaintenance.enfileirarManutenção ("BR-101", "29/03/2009")
queueMaintenance.enfileirarManutenção ("BR-317", "13/09/2010")
queueMaintenance.enfileirarManutenção ("BR-153", "22/05/2013")
queueMaintenance.enfileirarManutenção ("BR-364", "10/08/2015")
queueMaintenance.enfileirarManutenção ("BR-222", "14/10/2019")

nomeRodovia, dataManutenção = queueMaintenance.desenfileirar()
print ("Foi feita manutenção na rodovia", nomeRodovia, "na data", dataManutenção)