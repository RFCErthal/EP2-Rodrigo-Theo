def posiciona_frota(frota):
    
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    
    
    for navio, posicoes in frota.items():
        for lista_posicoes in posicoes:
            for pos in lista_posicoes:
                linha, coluna = pos
                tabuleiro[linha][coluna] = 1 
    
    return tabuleiro