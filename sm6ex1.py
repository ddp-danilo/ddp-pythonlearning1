def computador_escolhe_jogada(n, m):
    if n <= m: 
        return n 
    else:
        J = m 
        while J > 1:
            if ((n - J) % (m + 1)) == 0:
                return J
            else: 
                J -= 1
        return m 

def usuario_escolhe_jogada(n, m):
    loop = True
    while loop:
        u_jogada = input("Quantas peças você vai tirar? ")
        if (u_jogada <= str(m)) and (u_jogada >= '1'):
            return int(u_jogada)
        else:
            print("Oops! Jogada inválida! Tente de novo.")
def campeonato():
    partidas = 1
    pontos_p1 = 0
    pontos_cpu = 0
    while partidas <= 3:
        vc = 0
        print("**** Rodada", partidas, "****")
        vc = partida()
        partidas += 1
        if vc == 'CPU':
            pontos_cpu += 1
        if vc == 'P1':
            pontos_p1 += 1
    print("Placar: Você", pontos_p1, "X", pontos_cpu, "Computador")
    return 0

def test_cpu_win():
    assert computador_escolhe_jogada(1, 2) == 1
def test_cpu1():
    assert computador_escolhe_jogada(15, 3) == 3
def test_cpu2():
    assert computador_escolhe_jogada(22, 3) == 2




def partida(): 
    ultima_jogada = 0
    n = int(input("Quantas Peças? "))
    m = int(input("Limite de Peças por jogada? "))
    if ((n % (m + 1)) == 0) or m >= n:
        proxima_jogada = 'CPU'
        print("Computador começa!")
    else:
        proxima_jogada = 'P1'
        print("Você começa!")
    while n > 0:
        jogada = 0
        if (proxima_jogada == 'P1') and n > 0:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            if (jogada != 1) and (jogada > 0):
                print("Você tirou", jogada, "Peças")
            else:
                print("Você tirou uma Peça")
            proxima_jogada = 'CPU'

        if (proxima_jogada == 'CPU') and n > 0:
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
        return "CPU"
    if proxima_jogada == 'CPU':
        print('Fim do jogo! Você ganhou!')
        return "P1"



def main():
    cp = 1
    while cp == 1:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("1 - Para jogar uma partida isolada")
        escolha = input("2 - Para jogar um campeonato ")
        if (escolha == '1') or (escolha == '2'):
            if (escolha == '1'):
                print("Voce escolheu um Partida!")
                cp = partida()
            if (escolha == '2'):
                print("Voce escolheu um campeonato!")
                cp = campeonato()
        else:
            print("Opção errada tente novamente.")
 
        




main()
