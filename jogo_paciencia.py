# importando funções do jogo
from funcoes_de_trabalho import *
from time import sleep

# Introdução e regras do Jogo
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

# Algorito de Jogabilidade
input()
baralho= cria_baralho()

while possui_movimentos_possiveis(baralho) == True:
    for index, conteudo in enumerate(baralho):
        sleep(0.0001)
        print(f'{index + 1}. {cores(conteudo)}')
    escolha= int(input(f'Escolha uma carta (digite um número entre \033[1;33;40m{1}\033[m e \033[1;33;40m{len(baralho)}\033[m): '))

    cont2= escolha - 1

    if lista_movimentos_possiveis(baralho, cont2) == []:
        cont3= escolha-1
        baralho.append(baralho[cont3])
        print(f'A carta {cores(baralho[escolha-1])} não pode ser movida. Por favor, digite um número entre \033[1;33;40m{1}\033[m e \033[1;33;40m{len(baralho) - 1}\033[m): ')
        input('Clique ENTER para escolher uma nova carta')
    if len(lista_movimentos_possiveis(baralho, cont2)) == 1:

        if lista_movimentos_possiveis(baralho, cont2)[0] == 1:
            cont3= cont2 - 1

        if lista_movimentos_possiveis(baralho, cont2)[0] == 3:
            cont3= cont2 - 3

    if len(lista_movimentos_possiveis(baralho, cont2)) == 2:
        print(f'Sobre qual carta você quer emplihar o {cores(baralho[escolha - 1])}?')

        print(f'1. {cores(baralho[escolha - 2])}\n2. {cores(baralho[escolha - 4])}') 

        n= int()
        while n != 1 or n != 2:
            n= int(input(f'Digite o número de sua escolha (1-{len(baralho)}): '))
            if n == 1 or n == 2:
                break
        if n == 1:
            cont3= cont2 - 1
        if n == 2:
            cont3= cont2 - 3

    if len(baralho) == 1:
        print('FIM!')
        break

    baralho= empilha(baralho,cont2,cont3)

if possui_movimentos_possiveis(baralho) == False:
    print('Perdeu o Jogo,. Não tem mais movimentos possíveis!')