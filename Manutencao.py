from ArrayStack import ArrayStack


class Manutencao:
    def __init__(self, rodovia, data):
        self.rodovia = rodovia
        self.data = data

class HistoricoManu:
    def __init__(self):
        self._historico = ArrayStack()

    def registrar_manutencoes(self, rodovia, data):
        manutencao_obj = Manutencao(rodovia, data)
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
