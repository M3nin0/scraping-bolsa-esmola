'''
    Arquivo para retornar em formato de dicionário as informações coletadas 

    Autores:
    Lucas Varlesse: https://github.com/lucaslvs
    Felipe Menino: https://github.com/M3nin0
''' 

from time import sleep
from functions import *
from estados import *
from municipios import *

# Informe o ano requisitado e escolha a opção
# Opção 1 - Estados
# Opção 2 - Municipios
# Opção 3 - Todas as informações

# Exemplo de uso: getData(2007, 3)

def getData(ano, escolha):

    urlBase = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaPesquisaAcaoUF.asp?codigoAcao=006O&codigoFuncao=08&NomeAcao=Transfer%EAncia+de+Renda+Diretamente+%E0s+Fam%EDlias+em+Condi%E7%E3o+de+Pobreza+e+Extrema+Pobreza+%28Lei+n%BA+10%2E836%2C+de+2004%29&Exercicio='

    codigo = ''
    exibe = 0

    if(ano >= 2004 and ano <= 2007):
        codigo = '006O&'
        url = urlBase[0:89] + codigo + urlBase[94:] + str(ano)

    elif(ano >= 2008 and ano <= 2017):
        codigo = '8442&'
        url = urlBase[0:89] + codigo + urlBase[94:] + str(ano)

    obj = chamaUrl(url)

    valores = setValores(obj)
    cidades = setCidades(obj)
    pagina = setPaginas(obj)
    estados = getSiglas(obj)

    if(escolha == 1):
        mostraEstados(pagina, valores, cidades, url, exibe, 1)
    elif(escolha == 2):
        mostraMunicipio(estados, exibe, ano, codigo, 1)
    elif(escolha == 3):
        mostraEstados(pagina, valores, cidades, url, exibe, 1)
        mostraMunicipio(estados, exibe, ano, codigo, 1)