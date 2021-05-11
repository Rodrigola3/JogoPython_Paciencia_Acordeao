# importando biblioteca para o embaralhamento das cartas
from random import shuffle 

def cria_baralho():
    baralho= ['A♠', 'A♥', 'A♣', 'A♦','2♠', '2♥', '2♣', '2♦', '3♦','3♠', '3♥', '3♣', '4♦','4♠', '4♥', '4♣', '5♦','5♠', '5♥', '5♣', '6♦','6♠', '6♥', '6♣', '7♦','7♠', '7♥', '7♣', '8♦','8♠', '8♥', '8♣', '9♦','9♠', '9♥', '9♣', '10♦','10♠', '10♥', '10♣', 'J♦','J♠', 'J♥', 'J♣', 'Q♦','Q♠', 'Q♥', 'Q♣', 'K♦','K♠', 'K♥', 'K♣']
    shuffle(baralho)
    return baralho

def extrai_naipe(naipe):
    lista2= []
    for c in naipe:
        lista2.append(c)
    return lista2[-1]

def extrai_valor(baralho):
    valor= baralho[:-1] 
    return valor

def lista_movimentos_possiveis(baralho, cont): 
    novo= []
  
    if cont == 0:
        return novo
    if cont == 1 or cont == 2:
        if extrai_naipe(baralho[cont]) == extrai_naipe(baralho[cont - 1]) or  extrai_valor(baralho[cont]) == extrai_valor(baralho[cont - 1]):
            novo.append(1)
    if cont >= 3:
        if extrai_naipe(baralho[cont]) == extrai_naipe(baralho[cont - 3]) or  extrai_valor(baralho[cont]) == extrai_valor(baralho[cont - 3]):
            novo.append(3)
        if extrai_naipe(baralho[cont]) == extrai_naipe(baralho[cont - 1]) or  extrai_valor(baralho[cont]) == extrai_valor(baralho[cont - 1]):
            novo.append(1)
    return novo

def empilha(baralho, cont2,cont3):
    if cont2 == 0:
        return baralho
    if cont2 == 1 or cont2 == 2:
        if extrai_naipe(baralho[cont2]) == extrai_naipe(baralho[cont3]) or  extrai_valor(baralho[cont2]) == extrai_valor(baralho[cont3]):
            baralho[cont3] = baralho[cont2]
            del baralho[cont2]
    if cont2 >= 3:
        if extrai_naipe(baralho[cont2]) == extrai_naipe(baralho[cont3]) or  extrai_valor(baralho[cont2]) == extrai_valor(baralho[cont3]):
            baralho[cont3] = baralho[cont2]
            del baralho[cont2]
    elif cont3 == 0:
        return baralho
    return baralho

def possui_movimentos_possiveis(baralho):
    cont= 0
    while cont < len(baralho):
        if len(lista_movimentos_possiveis(baralho, cont)) >= 1:
            return True

        else:
            cont+=1
    return False

# defindo função para a implementação de cores no baralho
def cores(naipe):
    if extrai_naipe(naipe) == '♠':
        cor= f'\033[1;34;40m{naipe}\033[0m'
    if extrai_naipe(naipe) == '♥':
        cor= f'\033[1;31;40m{naipe}\033[0m'
    if extrai_naipe(naipe) == '♣':
        cor= f'\033[1;32;40m{naipe}\033[0m'
    if extrai_naipe(naipe) == '♦':
        cor= f'\033[1;35;40m{naipe}\033[0m'
    return cor