import random
def inicializar_Tabuleiro():
    '''
    Cria a estrutura do jogo
    '''
    tabuleiro = []
    for _ in range(3):
        tabuleiro.append([' ',' ',' '])
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    '''
    Printa o jogo atual na tela
    '''  
    print('    0  1  2')
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):    
                if j == 0:
                    print(f'{i}   ',tabuleiro[i][j], end='|')
                elif j == 1:
                    print(tabuleiro[i][j], end='|')
                else:
                    if i == 0 or i == 1:
                        print(tabuleiro[i][j],'\n   ---+-+---')
                    else:
                        print(tabuleiro[i][j])  

def imprime_menu_principal():
    '''
    Exibe o menu principal com as opcoes: 1-Jogador x Jogador 2-Jogador x Maquina(facil) 3-Jogador x Maquina(dificil) 4-Sair do programa
    '''
    while True:
        modo = int(input('Escolha o MODO de jogo:\n[1]-Jogador x Jogador\n[2]-Jogador x Maquina (nivel Facil)\n[3]-Jogador x Maquina (nivel Dificil)\n[4]-Sair\n: '))
        if modo > 0 and modo < 5:
            break
    return modo

def imprimir_pontuacao(modo, pontuacao_1, pontuacao_2):
    '''
    imprime o status do jogo (a pontuacao dos jogadores ou jogador e maquina).
    '''
    print('*----PONTUACAO----*')
    if modo == 1:
        print(f'Jogador 1: {pontuacao_1}')
        print(f'Jogador 2: {pontuacao_2}\n')
    else:
        (print(f'Usuario: {pontuacao_1}'))
        (print(f'Maquina: {pontuacao_2}\n'))

def leia_coordenada_linha():
    '''
    Escolhe a coordenada da linha
    '''
    lin = int(input('\nDigite a coordenada da linha em que deseja marcar: '))
    return lin

def leia_coordenada_coluna():
    '''
    Escolhe a coordenada da coluna
    '''   
    col = int(input('Digite a coordenada da coluna em que deseja marcar: '))
    return col

def posicao_valida(tabuleiro, linha, coluna):
    '''
    Valida se a posicao esta disponivel, Retorna TRUE ou FALSE
    '''
    if linha <=2  and coluna <=2:
        if tabuleiro[linha][coluna] == ' ':
            valida = True
        else: 
            print('\nPosicao ocupada, tente novamente\n')
            valida = False
    else:   
        print('\nPosicao invalida, tente novamente\n')
        valida = False
    return valida

def jogar(tabuleiro, jogador, linha, coluna):
    '''
    Altera a casa do tabuleiro da linha e coluna fornecida, a partir do parâmetro JOGADOR (X ou O)
    '''
    tabuleiro[linha][coluna] = jogador

def jogada_usuario(tabuleiro, jogador):
    '''
    Executa as funções que definem e validam a casa do tabuleiro (linha e coluna) e chama a função jogar().
    '''
    posicao_validada = False
    while posicao_validada == False:
        linha = leia_coordenada_linha()
        coluna = leia_coordenada_coluna()
        posicao_validada = posicao_valida(tabuleiro, linha, coluna)
    jogar(tabuleiro, jogador, linha, coluna) #executa a jogada

def verifica_velha(tabuleiro):
    '''
    verifica se o jogo empatou a partir da função movimentos_validos() que retorna uma lista de movimentos validos e, se a lista tiver um length 0, empata
    '''
    if len(movimentos_validos(tabuleiro))==0:
        return True
    
def verifica_vencedor(tabuleiro, jogador):
    '''
    verifica as formas de ganhar possíveis no tabuleiro
    '''

    #verifica se ganhou em alguma horizontal
    for linha in tabuleiro:
        if all(coluna == jogador for coluna in linha):
            return True

    #verifica se ganhou em alguma vertical    
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    #verifica se ganhou na diagonal 1 (Começa na esquerda em cima e termina na direita embaixo)   
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    
    #verifica se ganhou na diagonal 2 (Começa na direita em cima e termina na esquerda embaixo)
    elif all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    #Retorna false se ninguem ganhou ainda
    return False

def jogada_maquina_facil(tabuleiro, maquina):
    '''
    a partir do import random com o metodo random.choice ela seleciona algum item aleatoriamente da lista que a função movimentos_validos() retorna
    '''
    casa = random.choice(movimentos_validos(tabuleiro))
    linha = casa[0]
    coluna = casa[1]
    jogar(tabuleiro, maquina, linha, coluna) #executa a jogada

def jogada_maquina_dificil(tabuleiro, jogador_usuario, maquina):
    '''
    Recebe uma lista contendo a linha e coluna selecionada pela função melhor_casa() e chama a função jogar()
    '''
    casa = melhor_casa(tabuleiro, jogador_usuario, maquina)
    linha = casa[0]
    coluna = casa[1]
    jogar(tabuleiro,maquina,linha,coluna) #executa a jogada

def modo_jogador(modo):
    '''
    Modo de jogo Usuário x Usuário
    '''
    print('*--JOGADOR Nº1--*')

    jogador_1 = figura_escolhida_jogador()

    if jogador_1 == 'X':
        jogador_2 = 'O'
    else:
        jogador_2 = 'X'

    pontuacao_j1 = 0
    pontuacao_j2 = 0

    while (pontuacao_j1 or pontuacao_j2) != 3: #jogo continua enquanto nenhum dos dois atingir 3 pontos

        tabuleiro = inicializar_Tabuleiro()
        imprimir_pontuacao(modo, pontuacao_j1, pontuacao_j2)
        if pontuacao_j2 > pontuacao_j1 or (pontuacao_j1 == pontuacao_j2 and (pontuacao_j2>=1 and pontuacao_j1>=1)):
            turno_jogador = jogador_2

        else:
            turno_jogador = jogador_1

        while True:
            imprimir_tabuleiro(tabuleiro)
            if turno_jogador == jogador_1:
                print(f'Vez do jogador 1 ({jogador_1})')
                jogada_usuario(tabuleiro, jogador_1)
                turno_jogador = jogador_2

            else:
                print(f'Vez do jogador 2 ({jogador_2})')
                jogada_usuario(tabuleiro, jogador_2)
                turno_jogador = jogador_1

            if verifica_vencedor(tabuleiro, jogador_1):
                print(f'Jogador 1 ({jogador_1}) venceu!')
                pontuacao_j1+=1
                break
            elif verifica_vencedor(tabuleiro, jogador_2):
                print(f'Jogador 2 ({jogador_2}) venceu!')
                pontuacao_j2+=1
                break

            elif verifica_velha(tabuleiro):
                print('Deu velha. Empate!')
                break 
    
def modo_facil(modo):
    '''
    Modo de jogo Usuário x Máquina (fácil)
    '''
    print('*--JOGADOR USUARIO--*')

    jogador_usuario = figura_escolhida_jogador()

    if jogador_usuario == 'X':
        maquina = 'O'
    else:
        maquina = 'X'

    pontuacao_usuario = 0
    pontuacao_maquina = 0

    while (pontuacao_usuario or pontuacao_maquina) != 3:

        tabuleiro = inicializar_Tabuleiro()
        imprimir_pontuacao(modo, pontuacao_usuario, pontuacao_maquina)

        if (pontuacao_maquina>pontuacao_usuario) or ((pontuacao_usuario==pontuacao_maquina) and (pontuacao_usuario>0)):
            turno_jogador = maquina
        else:
            turno_jogador = jogador_usuario

        while True:
            imprimir_tabuleiro(tabuleiro)
            #usuario joga
            if turno_jogador == jogador_usuario:
                print(f'Vez do Usuario ({jogador_usuario})')
                jogada_usuario(tabuleiro, jogador_usuario)
                turno_jogador = maquina

            #maquina joga
            else:
                print(f'Vez da Maquina ({maquina})')
                jogada_maquina_facil(tabuleiro, maquina)
                turno_jogador = jogador_usuario

            if verifica_vencedor(tabuleiro, jogador_usuario):
                print(f'Usuário ({jogador_usuario} venceu!)')
                pontuacao_usuario+=1
                break

            elif verifica_vencedor(tabuleiro, maquina):
                print(f'Máquina ({maquina} venceu!)')
                pontuacao_maquina+=1
                break

            elif verifica_velha(tabuleiro):
                print('Deu velha. Empate!')
                break     
            
def modo_dificil(modo):
    '''
    Modo de jogo Usuário x Máquina (difícil)
    '''
    print('*--JOGADOR USUARIO--*')

    jogador_usuario = figura_escolhida_jogador()

    if jogador_usuario == 'X':
        maquina = 'O'
    else:
        maquina = 'X'

    pontuacao_usuario = 0
    pontuacao_maquina = 0

    while (pontuacao_usuario or pontuacao_maquina) != 3:

        tabuleiro = inicializar_Tabuleiro()
        imprimir_pontuacao(modo, pontuacao_usuario, pontuacao_maquina)

        if (pontuacao_maquina>pontuacao_usuario) or ((pontuacao_usuario==pontuacao_maquina) and (pontuacao_usuario>0)):
            turno_jogador = maquina
        else:
            turno_jogador = jogador_usuario

        while True:
            imprimir_tabuleiro(tabuleiro)
            #usuario joga
            if turno_jogador == jogador_usuario:
                print(f'Vez do Usuario ({jogador_usuario})')
                jogada_usuario(tabuleiro, jogador_usuario)
                turno_jogador = maquina

            #maquina joga
            else:
                print(f'Vez da Maquina ({maquina})')
                jogada_maquina_dificil(tabuleiro, maquina)
                turno_jogador = jogador_usuario

            if verifica_vencedor(tabuleiro, jogador_usuario):
                print(f'Usuário ({jogador_usuario} venceu!)')
                pontuacao_usuario+=1
                break

            elif verifica_vencedor(tabuleiro, maquina):
                print(f'Máquina ({maquina} venceu!)')
                pontuacao_maquina+=1
                break

            elif verifica_velha(tabuleiro):
                print('Deu velha. Empate!')
                break
            
#FUNCOES AUXILIARES (NAO CONSTA NOS REQUISITOS MAS SENTI A NECESSIDADE DE CRIA-LAS)
def figura_escolhida_jogador():
    '''
    Jogador 1 pode escolher com qual figura ele irá começar, o jogador 2 começará com a que restar
    '''
    while True:
        escolha = int(input('Escolha sua figura:\n[1]-X\n[2]-O\n: '))
        match escolha:
            case 1:
                escolha = 'X'
                return escolha
            case 2:
                escolha = 'O'
                return escolha
            case _:
                print('\nEscolha invalida')

def movimentos_validos(tabuleiro):
    '''
    coloca todos os movimentos validos em uma lista e retorna ela
    '''
    lista_movimentos=[]
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == ' ':
                lista_movimentos.append((linha, coluna))
    return lista_movimentos

def minimax(tabuleiro, is_maximizing, jogador_usuario, maquina):
    '''
    algoritmo minimax() (recursiva), verifica todas as probabilidades possíveis no jogo e retorna um int
    '''

    #CONDIÇÕES DE PARADA DA RECURSÃO
    if verifica_vencedor(tabuleiro, maquina): #retorna 1 no fim da previsão se a maquina vence
        return 1
    if verifica_vencedor(tabuleiro, jogador_usuario): #retorna -1 no fim da previsão se o usuario vence
        return -1
    if len(movimentos_validos(tabuleiro)) == 0: #retorna 0 no fim da previsão se empata
        return 0
    
    if is_maximizing: #jogada de "maximização", vez da MAQUINA jogar
        best_score = -float('inf') #numero infinito negativo
        for casa in movimentos_validos(tabuleiro): #usa a lista de movimentos validos que a função retorna para testar as casas
            tabuleiro[casa[0]][casa[1]] = maquina #executa as possíveis jogadas como maquina sendo casa[0]-linha e casa[1]-coluna

            #inicio da recursão, define is_maximizing como False para na proxima execução rodar a jogada do USUARIO
            score = minimax(tabuleiro, False, jogador_usuario, maquina) 

            tabuleiro[casa[0]][casa[1]] = ' ' #Desfaz a jogada feita
            best_score = max(best_score, score) #compara best_score com score e transforma best_score no maior valor a partir do seu retorno
        return best_score #retorna o maior valor (melhor chance de ganho para a maquina)
    
    else:#jogada de "minimização", vez do USUÁRIO jogar
        best_score = float('inf') #numero infinito positivo
        for casa in movimentos_validos(tabuleiro):
            tabuleiro[casa[0]][casa[1]] = jogador_usuario #executa as possíveis jogadas como usuario

            #define is_maximizing como True para na proxima execução rodar a jogada da MAQUINA
            score = minimax(tabuleiro, True, jogador_usuario, maquina)

            tabuleiro[casa[0]][casa[1]] = ' ' #Desfaz a jogada feita
            best_score = min(best_score, score)
        return best_score #retorna o menor valor (menor chance de ganho para a maquina)
    
def melhor_casa(tabuleiro, jogador_usuario, maquina):
    '''
    A partir da função minimax() descobre qual é o melhor movimento (conjunto de linha e coluna) para a maquina fazer, retorna uma tupla contendo a linha e a coluna a serem jogadas
    '''
    best_score = -float('inf') #best_score começa com o menor numero possivel (infinito negativo)
    best_move = None #best_move começa sem nenhum valor
    for casa in movimentos_validos(tabuleiro): #percorre a lista de tuplas que contém os movimentos validos no tabuleiro
        tabuleiro[casa[0]][casa[1]] = maquina #executa a jogada como maquina

        #chama a função maquina para calcular as possibilidades das jogadas seguintes, começa em False para calcular a proxima jogada do usuario
        score = minimax(tabuleiro, False, jogador_usuario, maquina) 

        tabuleiro[casa[0]][casa[1]] = ' ' #desfaz a jogada
        if score > best_score: 
            best_score = score #atribui o score como "best_score"
            best_move = casa
    return best_move #retorna uma tupla com a linha e coluna
#---------FIM FUNCOES AUXILIARES-------------------

def main():
    while True:
        modo = imprime_menu_principal()
        match modo:
            case 1:
                modo_jogador(modo)
            case 2:
                modo_facil(modo)
            case 3:
                modo_dificil(modo)
            case 4:
                break
            case _:
                print('Opção inválida')
print('fim')

main()