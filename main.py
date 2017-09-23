'''
## Objetivo Definido: 
- Mostrar o total de valores gasto por estado com o projeto bolsa familia de 2004 a 2017

- E listar as 2 cidades de todos os estados que mais gastaram com o projeto

Autores:
    Lucas Varlesse: https://github.com/lucaslvs
    Felipe Menino: https://github.com/M3nin0

'''

from time import sleep
from functions import *
from estados import *
from municipios import *


urlBase = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaPesquisaAcaoUF.asp?codigoAcao=006O&codigoFuncao=08&NomeAcao=Transfer%EAncia+de+Renda+Diretamente+%E0s+Fam%EDlias+em+Condi%E7%E3o+de+Pobreza+e+Extrema+Pobreza+%28Lei+n%BA+10%2E836%2C+de+2004%29&Exercicio='

codigo = ''

ano = int(input("Qual ano você deseja consultar ?\nValores disponiveis de 2004 a 2017\n"))

if(ano < 2004 or ano > 2017):
    print("Esse ano não está cadastrado!")
    exit(1)

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

exibe = 0

escolha = input("Escolha uma opção?\n" \
                "Os que mais gastaram\n1 - Estado\n2 - Municipio\n" \
                "3 - As informações dos estados e dos muninicios\n")


if(escolha == '1'):
    print('Os estados que mais gastaram em ' + str(ano) + ' foram:\n')
    sleep(2)
    mostraEstados(pagina, valores, cidades, url, exibe, 0)

elif(escolha == '2'):
    print('Os municipios que mais gastaram em ' + str(ano) + ' foram:\n')
    sleep(2)
    mostraMunicipio(estados, exibe, ano, codigo, 0)

elif(escolha == '3'):
    print('Abaixo, valores de todos os gastos de estados e municipios em ' + str(ano) + '\n')
    sleep(3)
    mostraEstados(pagina, valores, cidades, url, exibe, 0)
    mostraMunicipio(estados, 1, ano, codigo, 0)