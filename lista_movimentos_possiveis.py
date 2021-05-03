def extrai_naipe(carta):

    naipe = carta[-1]

    return naipe



def extrai_valor(carta):

    valor= carta[:-1]

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