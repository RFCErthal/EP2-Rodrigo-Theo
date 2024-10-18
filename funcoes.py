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