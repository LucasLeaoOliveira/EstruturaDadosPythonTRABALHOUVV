from tadFila import ArrayQueue
from tadPilha import ArrayStack


class Manutencao:

    def __init__(self, rodovia, data):
        self.rodovia = rodovia
        self.data = data



class FilaManutencoes:

    def __init__(self):
        self.fila = ArrayQueue()



    def agendar_manutencao(self, rodovia, data):
        manutencao = Manutencao(rodovia, data)
        self.fila.enqueue(manutencao)



    def realizar_manutencao(self):
        if not self.fila.is_empty():
            manutencao = self.fila.dequeue()
            print(f"Realizando manutenção na rodovia {manutencao.rodovia} na data {manutencao.data}")
        else:
            print("Não há manutenções agendadas.")


    def concluir_manutencao(self):
        if not self.fila.is_empty():
            manutencao = self.fila.dequeue()
            print(f"Manutenção concluída na Rodovia {manutencao.rodovia} em {manutencao.data}")
        else:
            print("Não há manutenções agendadas.")


class HistoricoManutencoes:

    def __init__(self):
        self.pilha = ArrayStack()


    def registrar_manutencao(self, rodovia, data):
        manutencao = Manutencao(rodovia, data)
        self.pilha.push(manutencao)


    def mostrar_historico(self):
        print("Histórico de Manutenções:")
        while not self.pilha.is_empty():
            manutencao = self.pilha.pop()
            print(f"Rodovia: {manutencao.rodovia}, Data: {manutencao.data}")

class PilhaHistoricoManutencoes:
    def __init__(self):
        self.pilha = ArrayStack()

    def adicionar_manutencao_concluida(self, rodovia, data):
        manutencao = Manutencao(rodovia, data)
        self.pilha.push(manutencao)

    def exibir_historico(self):
        print("Histórico de Manutenções Concluídas:")
        while not self.pilha.is_empty():
            manutencao = self.pilha.pop()
            print(f"Rodovia: {manutencao.rodovia}, Data: {manutencao.data}")

