from functions import *

def mostraMunicipio(estados, exibe, ano, codigo):

    #print(estados)

    Gurl = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaPesquisaAcaoMunicipio.asp?Exercicio=2017&textoPesquisaAcao=&codigoAcao=8442&codigoFuncao=08&siglaEstado=AC'
    
    Gurl = Gurl[0:95] + str(ano) + Gurl[99:130] + codigo + Gurl[135:]

    url = Gurl 

    Gurl = setSiglaUrl(Gurl, estados[0])

    obj = chamaUrl(url)

    pagina = setPaginas(obj)

    if(getNumeroPagina(pagina) != 1):

        index = 1

        valores = setValores(obj)
        cidades = setCidades(obj)
        
        verificaValor(valores, cidades, 'municipio', exibe)
        getMaiorMunicipio(exibe)

        while(index < len(estados) - 1):

            cont = 1

            while(True):

                cont += 1

                valores = setValores(obj)
                cidades = setCidades(obj)

                verificaValor(valores, cidades, 'municipio', exibe)
                getMaiorMunicipio(exibe)

                url += '&Pagina=' + str(cont)

                obj = chamaUrl(url)

                valores = setValores(obj)
                cidades = setCidades(obj)

                verificaValor(valores, cidades, 'municipio', exibe)
                getMaiorMunicipio(exibe)
    
                if(cont <= getNumeroPagina(pagina)):

                    index += 1
                    url = setSiglaUrl(Gurl, estados[index])
                    obj = chamaUrl(url)
                    break
   
    else:
        verificaValor(valores, cidades, 'municipio', exibe)
        getMaiorMunicipio(exibe)