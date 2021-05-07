from funcoes_de_trabalho import *
from time import sleep
print(  '''

    Paciência Acordeão 
    ================== 

    Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

    Existem apenas dois movimentos possíveis: 

    1. Empilhar uma carta sobre a carta imediatamente anterior; 
    2. Empilhar uma carta sobre a terceira carta anterior. 

    Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

    1. As duas cartas possuem o mesmo valor ou 
    2. As duas cartas possuem o mesmo naipe. 

    Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

    Aperte [Enter] para iniciar o jogo... 

        '''
)

input()
baralho= cria_baralho()

while possui_movimentos_possiveis(baralho) == True:
    for index, conteudo in enumerate(baralho):
        sleep(0.1)
        print(f'{index + 1}. {conteudo}')
    escolha= int(input(f'Escolha uma carta (digite um número entre 1 e {len(baralho)}: '))

    cont2= escolha - 1
    if len(lista_movimentos_possiveis(baralho, cont2)) == 1:

        if lista_movimentos_possiveis(baralho, cont2)[0] == 1:
            cont3= cont2 - 1

        if lista_movimentos_possiveis(baralho, cont2)[0] == 3:
            cont3= cont2 - 3

    if len(baralho) == 1:
        print('FIM!')
        break

    baralho= empilha(baralho,cont2,cont3)