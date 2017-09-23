from functions import *

def mostraEstados(pagina, valores, cidades, url, exibe, api):

    estados = []

    #Mostra o valor gasto por estado
    if(getNumeroPagina(pagina) != 1):

        verificaValor(valores, cidades, 'estado', exibe)
        
        if(api == 0):
            getMaiorEstado(exibe)
        else:
            estados.append(returnMaiorEstado())

        cont = 1

        #Verifica a quantidade de páginas e faz a exibição dos itens
        while(True):

            cont += 1

            url += '&Pagina=' + str(cont)

            obj = chamaUrl(url)

            valores = setValores(obj)
            cidades = setCidades(obj)

            verificaValor(valores, cidades, 'estado', exibe)

            if(api == 0):
                getMaiorEstado(exibe)
            else:
                estados.append(returnMaiorEstado())

            if(cont == getNumeroPagina(pagina)):
                break

    else:
        verificaValores(valores, cidades, 'estado')

        if(api == 0):
            getMaiorEstado(exibe)
        else:
            estados.append(returnMaiorEstado())

    return estados