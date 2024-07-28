import time
from collections import deque

def lerLabirinto(arquivo):
    with open(arquivo, 'r') as file:
        labirinto = [list(linha.strip()) for linha in file.readlines()]
    return labirinto

def encontrarPosicao(labirinto, char):
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == char:
                return (i, j)
    return None

def construirListaAdjacencia(labirinto):
    adj = {}
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula != '#':
                adj[(i, j)] = []
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(labirinto) and 0 <= nj < len(labirinto[0]) and labirinto[ni][nj] != '#':
                        adj[(i, j)].append((ni, nj))
    return adj

def buscaLargura(adj, inicio, fim):
    queue = deque([inicio])
    visited = set([inicio])
    parent = {inicio: None}
    pontosVisitados = [inicio]

    while queue:
        atual = queue.popleft()
        if atual == fim:
            break
        for vizinho in adj[atual]:
            if vizinho not in visited:
                queue.append(vizinho)
                visited.add(vizinho)
                parent[vizinho] = atual
                pontosVisitados.append(vizinho)

    path = []
    passo = fim
    while passo:
        path.append(passo)
        passo = parent.get(passo)
    path.reverse()
    return path if path and path[0] == inicio else None, pontosVisitados

def buscaProfundidade(adj, inicio, fim):
    stack = [inicio]
    visited = set([inicio])
    parent = {inicio: None}
    pontosVisitados = [inicio]

    while stack:
        atual = stack[-1]  
        if atual == fim:
            break
        
        for vizinho in adj[atual]:
            if vizinho not in visited:
                stack.append(vizinho)
                visited.add(vizinho)
                parent[vizinho] = atual
                pontosVisitados.append(vizinho)
                break
        else:
            stack.pop()

    path = []
    passo = fim
    while passo:
        path.append(passo)
        passo = parent.get(passo)
    path.reverse()
    return path if path and path[0] == inicio else None, pontosVisitados

def main():
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        try:
            labirintoLargura = lerLabirinto(arquivo)
            labirintoProfundidade = lerLabirinto(arquivo)

            inicio = encontrarPosicao(labirintoLargura, 'S')
            fim = encontrarPosicao(labirintoLargura, 'E')

            if not inicio or not fim:
                print("Labirinto invalido. Certifique-se de que há um 'S' e um 'E' no labirinto.")
                continue

            listaAdjLargura = construirListaAdjacencia(labirintoLargura)
            listaAdjProfundidade = construirListaAdjacencia(labirintoProfundidade)

            while True:
                metodo = input("Escolha o metodo:\n 1 para Busca em Largura\n 2 para Busca em Profundidade\n 0 para sair: ")
                if metodo == '0':
                    break
                elif metodo == '1':
                    startTime = time.time()
                    caminhoLargura, pontosVisitadosLargura = buscaLargura(listaAdjLargura, inicio, fim)
                    endTime = time.time()
                    if caminhoLargura:
                        print("\nCaminho:", ' '.join(map(str, caminhoLargura)))
                    else:
                        print("Nenhum caminho encontrado pela Busca em Largura.")
                    print("\nPontos visitados pela Busca em Largura:", pontosVisitadosLargura)
                    print("\nTempo:", endTime - startTime, "s\n")
                elif metodo == '2':
                    startTime = time.time()
                    caminhoProfundidade, pontosVisitadosProfundidade = buscaProfundidade(listaAdjProfundidade, inicio, fim)
                    endTime = time.time()
                    if caminhoProfundidade:
                        print("\nCaminho:", ' '.join(map(str, caminhoProfundidade)))

                    else:
                        print("Nenhum caminho encontrado pela Busca em Profundidade.")
                    print("\nPontos visitados pela Busca em Profundidade:", pontosVisitadosProfundidade)
                    print("\nTempo:", endTime - startTime, "s\n")
                else:
                    print("Metodo invalido. Escolha 1 para Largura ou 2 para Profundidade.")
                    continue

        except FileNotFoundError:
            print("Arquivo nao encontrado. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
