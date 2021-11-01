"""
def usuario_escolhe_jogada():
def computador_escolhe_jogada():
    Devem ter esses nomes.
    Devem receber exatamente dois parametros.
    Devem funcionar sozinhas.
    Devem devolver o número de peças removidas pela jogada.


def partida():
    é quem pergunta os valores de n e m que valem na partida
    é quem decide quem começa o jogo
    é quem é responsável por chamar an "funções escolhe_jogadas()" alternadamentei
    é quem recebe o valor develvido por essas funções e atualiza o valor de n de acordo.
    é quem identifica que o jogo acabou (n == 0).


Erros comuns
 || Para alternar entre os jogadores
 ||     Computader_escolhe_jogada(), apos terminar, chama usuario_escolhe_jogada() e vice-versa
 ||         mas nesse caso s funções não devolvem nada!
 || ..._escolhe_jogada(), devolve o número de peças restantes no tabuleiro
 ||     mas o pedido foi o número de peças removidas!
 || Os valores de n e m são globais
        mas então os parametros das funções são inúteis!
        as funções não são mais indenpentdentes

Dicas e Pegadinhas
    Depois de definir todas funções necessárias, é preciso iniciar o jogo de alguma maneira
        ...print("Bem Vindo")
        Função "jogo()", "main()", "inicio()" etc.
    Para checar se a entrada do usuário é válida, é so fazer um laço usando uma condiçao booleano
    Ha varios erros possíveis do corretor automático 

Corretor automático
    Testando validação de entrada do usuário (n = X, rosposta Z)
        usuario_escolhe_jogada(X, Y), usuario "digita" Z
    Testando a jogada da computador (n = X, m = Y) 
        computador_escolhe_jogada()
    Checando Partida Unica (n = x, jogadas =(A, B, C,,,)
        Roda o programa, escolhe a opção 1, informa X e Y e faz as jogdas.
    Checando Campeonato 
        roda o programa, escolhe a opção 2 e roda tres partidas seguidas.
    Não esqueça as mensagens!
    "... Começa!"
    "... Venceu!"

"""

