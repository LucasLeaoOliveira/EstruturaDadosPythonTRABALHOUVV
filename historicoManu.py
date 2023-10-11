from ArrayStack import *

class Manutencao:
    def __init__(self, rodovia, data):
        self.rodovia = rodovia
        self.data = data

class HistoricoManu:
    def __init__(self):
        self._historico = ArrayStack()

    def registrar_manutencoes(self, rodovia, data):
        manutencao_obj = Manutencao(rodovia, data)  # Renomeei a variável para evitar conflito com o nome da classe
        self._historico.push(manutencao_obj)

    def obter_historico(self):
        historico = []
        copia = ArrayStack()

        while not self._historico.is_empty():
            man = self._historico.pop()
            historico.append((man.rodovia, man.data))
            copia.push(man)

        while not copia.is_empty():
            self._historico.push(copia.pop())

        return historico

historico = HistoricoManu()
historico.registrar_manutencoes("Rodovia z", "2023-02-10")
historico.registrar_manutencoes("Rodovia y", "2023-05-20")
historico.registrar_manutencoes("Rodovia C", "2023-12-25")

print("Histórico de Manutenções:")
for rodovia, data in historico.obter_historico():
    print(f"Rodovia: {rodovia}, Data: {data}")