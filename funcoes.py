def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    while tamanho > 0:
        if orientacao == "vertical":
            posicoes.append([linha, coluna])
            linha += 1  
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna])
            coluna += 1  
        
        tamanho -= 1  
    
    return posicoes 


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_navio)
    else:
        frota[nome_navio] = [posicoes_navio]
    
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'  
    else:
        tabuleiro[linha][coluna] = '-'  
    
    return tabuleiro


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


def afundados(frota, tabuleiro):
    navios_afundados = 0
    
    for navio, posicoes in frota.items():
        for lista_posicoes in posicoes:
            afundado = 1  
            
            
            for pos in lista_posicoes:
                linha, coluna = pos
                if tabuleiro[linha][coluna] != 'X':
                    afundado = 0
                    break
        
            navios_afundados += afundado
                
    return navios_afundados


def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for pos in posicoes_novo_navio:
        linha_pos, coluna_pos = pos
        if linha_pos > 9 or coluna_pos > 9:
            return False
    
    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                if posicao in posicoes_novo_navio:
                    return False
    
    return True


