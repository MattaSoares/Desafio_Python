# Desafio 114 - Site está acessivel?
''' Crie um código em Python que teste se o site Pudim está acessível pelo computador'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está disponível no momento')
else:
    print('Site Pudim acessado com sucesso')
