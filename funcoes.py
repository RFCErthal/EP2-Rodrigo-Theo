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