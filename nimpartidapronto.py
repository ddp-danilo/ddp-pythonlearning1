def computador_escolhe_jogada(n, m):# Jogada da cpu testado
    if n <= m: #se o numero de peças for menor que a quantidade de pecas que pode ser removida
        return n #Remove todas
    else:
        J = m #Da a J o valor de m
        while J > 1:
            if ((n - J) % (m + 1)) == 0:#testa se n - j da u numero multiplo de (m mais 1) se sim Devolve j caso contrario subtrai 1 de j
                return J
            else: 
                J -= 1
        return 1 # se todo o resto der errado retorne 1


def test_cpu_win():
    assert computador_escolhe_jogada(1, 2) == 1
def test_cpu1():
    assert computador_escolhe_jogada(15, 3) == 2
def test_cpu2():
    assert computador_escolhe_jogada(22, 3) == 1

def campeonato(X):
    print('ok')
 
def partida():
    ultima_jogada = 0
    n = int(input("Quantas Peças? "))
    m = int(input("Limite de Peças por jogada? "))
    if ((n % (m + 1)) == 0) or (n == 1):
        proxima_jogada = 'CPU'
        print("Computador começa!")
    else:
        proxima_jogada = 'P1'
        print("Você começa!")
    while n > 0:
        jogada = 0
        if (proxima_jogada == 'P1'):
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if (jogada != 1) and (jogada > 0):
                print("Você tirou", jogada, "Peças")
            else:
                print("Você tirou uma Peça")
            proxima_jogada = 'CPU'

        if (proxima_jogada == 'CPU'):
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            if (jogada != 1) and (jogada > 0):
                print("O computador tirou", jogada, "Peças.")
            else:
                print("O Computador tirou uma Peça.")
            proxima_jogada = 'P1'
        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        if (n > 1):
            print("Agora restam", n, "Peças no tabuleiro.")
    if proxima_jogada == 'P1':
        print('Fim do jogo! O computador ganhou!')
    if proxima_jogada == 'CPU':
        print('Fim do jogo! Você ganhou!')



def main():
    cp = 1
    while cp == 1:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("1 - Para jogar uma partida isolada")
        escolha = input("2 - Para jogar um campeonato ")
        if (escolha == '1') or (escolha == '2'):
            if (escolha == '1'):
                partida()
            if (escolha == '2'):
                campeonato()
        else:
            print("Opção errada tente novamente.")
 
        


def usuario_escolhe_jogada(n, m):#Testado
    loop = True
    while loop:
        u_jogada = input("Quantas peças você vai tirar? ")
        if (u_jogada <= str(m)) and (u_jogada >= '1'):
            return int(u_jogada)
        else:
            print("Oops! Jogada inválida! Tente de novo.")


