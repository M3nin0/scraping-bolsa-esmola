'''
Funções criadas para auxiliar a busca por informações no site da transparência

Autores:
    Lucas Varlesse: https://github.com/lucaslvs
    Felipe Menino: https://github.com/M3nin0

(Estados) == Que a função se refere a página onde os estados são listados
(Municipios) == Que a função se refere a página onde os municipios são listados

'''

import string
import requests as request
from urllib.request import urlopen
from bs4 import BeautifulSoup

estado = {}
municipio = {}

#Exibe a relação de cidade x gastos com bolsa familia (Estados)
def verificaValor(valores, cidades, tipo, exibe):
    cont = 2

    if(tipo == 'estado'):

        for i in valores[2:]:
            
            temp = i.text.replace(' ', '')

            if(exibe == 1):
                print('Estado: ' + cidades[cont].text + '\nValor total recebido: ' + temp)
            
            temp = temp.replace('\r\n', '')
            temp = temp.replace(',', '')
            temp = temp.replace('.', '')

            global estado
            estado[int(temp)] = cidades[cont].text

            cont += 1

    if(tipo == 'municipio'):
        
        for i in valores[2:]:
            
            temp = i.text.replace(' ', '')

            if(exibe == 1):
                print('Municipio de : ' + cidades[cont].text + '\nValor total recebido: ' + temp)
            
            temp = temp.replace('\r\n', '')
            temp = temp.replace(',', '')
            temp = temp.replace('.', '')

            global municipio
            municipio[temp] = cidades[cont].text

            cont += 1

#Devolve a quantidade de páginas que o site tem (Estados)
def getNumeroPagina(pagina):

    num = ''

    for i in pagina:

        num = i.find('p').text

    return int(num[9])

#Puxa a html da url passada (Estados)
def chamaUrl(url):

    r = request.get(url)

    return BeautifulSoup(r.content, 'html.parser')

#Devolve todos os textos que tem td com a classe colunaValor (Estados)
def setValores(obj):

    valores = obj.findAll('td', {'class': 'colunaValor'})

    return valores

#Devolve todas os textos que div com id paginacao (Estados)
def setPaginas(obj):

    paginas = obj.findAll('div', attrs = {'id': 'paginacao'})

    return paginas

#Devolve todos os textos que tem td com a classe firstChild (Estados)
def setCidades(obj):

    cidades = obj.findAll('td', {'class': 'firstChild'})

    return cidades

#Pega todos as siglas de estados (Estados)
def getSiglas(obj):

    estados = []

    archor = obj.findAll('a')

    for i in archor:
        if i['href'][0:44] == 'PortalTransparenciaPesquisaAcaoMunicipio.asp':
            estados.append(i['href'][-2:])
    
    return estados

#Coloca a sigla na url (Municipios)
def setSiglaUrl(url, sigla):

    nova = url[:-2]

    return nova + sigla

#Retorna o estado que mais gastou 
def getMaiorEstado(exibe):

    global estado 
    
    maiores = sorted(estado, reverse = True)[:3]

    if(exibe == 0):
        for i in range(0, 3):
            print('Nome: ' + estado[maiores[i]] + '\nValor gasto: ' + str(maiores[i]))

    estado = {}

#Retorna o municipio que mais gastou
def getMaiorMunicipio(exibe):

    global municipio
    
    maiores = sorted(municipio, reverse = True)[:3]
    
    if(exibe == 0):
        for i in range(0, 2):
            print('Nome: ' + municipio[maiores[i]] + '\nValor gasto: ' + str(maiores[i]))

    municipio = {}
    