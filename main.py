from Manutencao import HistoricoManu
from Fila import Fila
from Rodovia import Rodovia


def main():
    # Exemplo de uso da classe HistoricoManu
    historico = HistoricoManu()
    historico.registrar_manutencoes("Rodovia A", "2023-01-01")
    historico.registrar_manutencoes("Rodovia B", "2023-01-02")

    print("Histórico de Manutenções:")
    for rodovia, data in historico.obter_historico():
        print(f"Rodovia: {rodovia}, Data: {data}")

    # Exemplo de uso da fila de manutenções
    queueMaintenance = Fila()
    queueMaintenance.enfileirarManutencao("BR-262", "20/07/2014")
    queueMaintenance.enfileirarManutencao("BR-230", "17/07/2007")

    nomeRodovia, dataManutencao = queueMaintenance.desenfileirar()
    if nomeRodovia:
        print("Foi feita manutenção na rodovia", nomeRodovia, "na data", dataManutencao)

    # Uso das funções da classe Rodovia
    rodovias = Rodovia.ler_arquivo('arquivo.txt')  # Lê o arquivo texto
    print("\nRodovias e suas cidades:")
    for rodovia in rodovias:
        cidades = ', '.join(rodovia.cidades)
        print(f"Rodovia: {rodovia.nome}, Cidades: {cidades}")


if __name__ == "__main__":
    main()