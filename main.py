import time
from busca import BuscaLargura, BuscaProfundidade

def ler_labirinto(arquivo):
    with open(arquivo, 'r') as f:
        labirinto = [list(linha.strip()) for linha in f.readlines()]
    return labirinto

def construir_lista_adjacencia(labirinto):
    lista_adj = {}
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] != '#':
                lista_adj[(i, j)] = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(labirinto) and 0 <= nj < len(labirinto[0]) and labirinto[ni][nj] != '#':
                        lista_adj[(i, j)].append((ni, nj))
    return lista_adj

def encontrar_posicao(labirinto, char):
    for i, linha in enumerate(labirinto):
        for j, c in enumerate(linha):
            if c == char:
                return i, j
    return None

def main():
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        try:
            labirinto = ler_labirinto(arquivo)
            inicio = encontrar_posicao(labirinto, 'S')
            fim = encontrar_posicao(labirinto, 'E')

            if not inicio or not fim:
                print("Labirinto inválido. Certifique-se de que há um 'S' e um 'E' no labirinto.")
                continue

            lista_adj = construir_lista_adjacencia(labirinto)

            while True:
                metodo = input("Escolha o método:\n 1 para Busca em largura\n 2 para Busca em profundidade\n 0 para sair0: ")
                if metodo == '0':
                    break
                elif metodo == '1':
                    start_time = time.time()
                    caminho = BuscaLargura(lista_adj, inicio, fim)
                    end_time = time.time()
                elif metodo == '2':
                    start_time = time.time()
                    caminho = BuscaProfundidade(lista_adj, inicio, fim)
                    end_time = time.time()
                else:
                    print("Método inválido. Escolha 1 para BFS ou 2 para DFS.")
                    continue

                if caminho:
                    print("Caminho:", ' '.join(map(str, caminho)))
                else:
                    print("Nenhum caminho encontrado.")
                print("Tempo:", end_time - start_time, "s")

        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()