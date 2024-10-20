from funcoes import posicao_valida, define_posicoes, preenche_frota

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

embarcacoes = [
    ("porta-aviões", 4),
    ("navio-tanque", 3),
    ("navio-tanque", 3),
    ("contratorpedeiro", 2),
    ("contratorpedeiro", 2),
    ("contratorpedeiro", 2),
    ("submarino", 1),
    ("submarino", 1),
    ("submarino", 1),
    ("submarino", 1),
]

def posicionar_frota(frota):
    for nome, tamanho in embarcacoes:
        while True:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            else:
                orientacao = "horizontal" 

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                break
            
            else:
                print("Esta posição não está válida!")
    return frota

frota_atualizada = posicionar_frota(frota)
print(frota_atualizada)
