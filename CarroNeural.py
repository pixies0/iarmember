import numpy as np
import random


class CarroNeural:
    def __init__(self, pesos=None):
        if pesos is None:
            # 5 sensores -> 4 ocultos -> 2 saídas (girar ou não)
            self.peso1 = np.random.rand(5, 4)  # Pesos para a primeira camada
            self.peso2 = np.random.rand(4, 2)  # Pesos para a segunda camada

        else:
            self.peso1, self.peso2 = pesos

    def pensar(self, sensores):
        oculto - np.tanh(sensores @ self.peso1)
        saida = np.tanh(oculto @ self.peso2)
        direcao = saida[0]
        gasolina = saida[1]
        return direcao, gasolina

    def mutacao(self):
        # Aplica mutação aos pesos
        self.peso1 = np.random.rand(5, 4) * 0.3
        self.peso2 = np.random.rand(4, 2) * 0.3


def nova_geracao(carros, pontos):
    topo = sorted(zip(carros, pontos), key=lambda x: -x[0])[: len(carros) // 5]
    novos_carros = []
    for _ in range(len(carros)):
        pai = random.choice(topo)[1]
        filho = CarroNeural(pesos=(pai.peso1.copy(), pai.peso2.copy()))
        filho.mutacao()
        novos_carros.append(filho)
    return novos_carros
