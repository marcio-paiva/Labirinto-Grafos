def BuscaLargura(ListaAdj, s, e):
    visitado = {v: False for v in ListaAdj}
    visitado[s] = True
    f = [s]
    caminho = {s: [s]}

    while len(f) != 0:
        u = f.pop(0)
        for v in ListaAdj[u]:
            if not visitado[v]:
                visitado[v] = True
                f.append(v)
                caminho[v] = caminho[u] + [v]
                if v == e:
                    return caminho[v]
    return None


def BuscaProfundidade(ListaAdj, s, e):
    visitado = {v: False for v in ListaAdj}
    visitado[s] = True
    f = [s]
    caminho = {s: [s]}

    while len(f) != 0:
        u = f[-1]
        ExisteAdj = False 
        for v in ListaAdj[u]:
            if not visitado[v]:
                ExisteAdj = True
                visitado[v] = True
                f.append(v)
                caminho[v] = caminho[u] + [v]
                if v == e:
                    return caminho[v]
                break 
        
        if not ExisteAdj:
            f.pop()

    return None  