from funcoes import posicao_valida, define_posicoes, preenche_frota, afundados, faz_jogada

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
                orientacao = int(input("Orientação: [1] Vertical [2] Horizontal "))
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
# print(frota_atualizada)

# pergunta 8

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

# Frota do oponente
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = [['0' for coluna in range(10)] for linha in range(10)]
tabuleiro_oponente = [['0' for coluna in range(10)] for linha in range(10)]

for navio, posicoes in frota_oponente.items():
    for posicao in posicoes:
        for coordenada in posicao:
            linha, coluna = coordenada
            tabuleiro_oponente[linha][coluna] = 'N' 

for navio, posicoes in frota.items():
    for posicao in posicoes:
        for coordenada in posicao:
            linha, coluna = coordenada
            tabuleiro_jogador[linha][coluna] = '1'

jogando = True
jogadas_realizadas = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input("Jogador, qual linha deseja atacar? "))

    coluna = int(input("Jogador, qual coluna deseja atacar? "))  
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input("Jogador, qual coluna deseja atacar? "))  

    while (linha, coluna) in jogadas_realizadas:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))  
        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input("Jogador, qual coluna deseja atacar? "))  

    jogadas_realizadas.append((linha, coluna))
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(tabuleiro_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
