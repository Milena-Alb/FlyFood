import itertools
import time

def lerMatriz(arquivo):
    with open(arquivo, 'r') as rota:
        linhas = rota.readlines()
    dimensoes_matriz = list(map(int, linhas[0].strip().split()))
    matriz = []
    pontos_matriz = {}
    ponto_origem = None
    for i in range(dimensoes_matriz[0]):
        linha = linhas[i + 1].strip().split()
        matriz.append(linha)
        for j in range(dimensoes_matriz[1]):
            if linha[j] != '0' and linha[j] != 'R':
                pontos_matriz[linha[j]] = (i, j)
            elif linha[j] == 'R':
                ponto_origem = (i, j)
    return matriz, pontos_matriz, ponto_origem

def calcularDistancia(ponto_1, ponto_2):
    return abs(ponto_1[0] - ponto_2[0]) + abs(ponto_1[1] - ponto_2[1])

def menorPercurso(pontos, ponto_origem):
    menor_percurso = None
    menor_distancia = float('inf')
    pontos_chave = list(pontos.keys())
    permutacoes = itertools.permutations(pontos_chave)

    for permutacao in permutacoes:
        distancia_total = 0
        ponto_atual = ponto_origem
        for ponto in permutacao:
            distancia_total += calcularDistancia(ponto_atual, pontos[ponto])
            ponto_atual = pontos[ponto]
        distancia_total += calcularDistancia(ponto_atual, ponto_origem)
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            menor_percurso = permutacao
    return menor_percurso, menor_distancia

def main():
    inicio = time.time()
    arquivo = '.\matrizes_testes\matriz_teste4.txt'
    matriz, pontos_matriz, ponto_origem = lerMatriz(arquivo)
    menor_percurso_resultado, menor_distancia = menorPercurso(pontos_matriz, ponto_origem)

    print("\nMenor percurso encontrado:")
    print(f"{' '.join(menor_percurso_resultado)}: {menor_distancia} dronômetros")

    fim = time.time() 
    duracao = fim - inicio  
    print(f"Tempo de execução: {duracao: .5f} segundos")

if __name__ == "__main__":
    main()