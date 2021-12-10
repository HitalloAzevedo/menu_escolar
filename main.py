from math import log
from interface import *
from calculos import *

author = 'Hitallo Azevedo'
version = 'v0.0.1'
# Muito obrigado pela preferência Github: @HitalloAzevedo

cabecalho(f'MENU ESCOLAR {version}')
print(f'Criado por {author}')
print('=' * 60)

opcao = menu('Progressão Aritmética',
'Progressão Geométrica',
'Fibonacci',
'Função Primeiro Grau',
'Função Segundo Grau',
'Logaritmo')

print(opcao)

