import os
from typing import List

def menu(*options):
    i = 1
    for opt in options:
        if opt == 'SAIR':
            i = 99
        print(f'{i}'.zfill(2) + ' - ' + f'{opt}')
        i += 1
    
    print('sua opção >>> ', end='')
    opcao = getIntegerNumber()
    return opcao

def drawHeader(content:str, tam=60, simb='=', clearTerminal=True):
    if clearTerminal:
        clear()
    for line in content:
        print(simb * tam)
        print(line[1].center(tam) if line[0] == True else line[1])
        print(simb * tam)

def getIntegerNumber():
    while True:
        try:
            value = int(input())
            return value
        except (ValueError, TypeError):
            print('Insira um valor inteiro!') 

def getRealNumber():
    while True:
        try:
            value = float(input())
            return value
        except (ValueError, TypeError):
            print('Por favor insira um valor válido!') 

def showSequence(sequence: List[float]):
    for i, e in enumerate(sequence):
        if i < len(sequence) - 1:
            print(int(e) if e.is_integer() else e, end=' -> ')
        else:
            print(int(e) if e.is_integer() else e, '-> Fim')

# def subs(n):
#     subs = {
#         0: '\u2080', 
#         1: '\u2081', 
#         2: '\u2082', 
#         3: '\u2083', 
#         4: '\u2084', 
#         5: '\u2085', 
#         6: '\u2086',
#         7: '\u2087',
#         8: '\u2088',
#         9: '\u2089',
#     }

#     string = []

#     if n > 9:
#         n = integerFormat(n)
#         n = str(n)
#         for i in n:
#             if i != '.':
#                 i = subs.get(int(i))
#             string.append(i)
#         string = ''.join(string)
#         return string
    
#     return subs.get(n)

def integerFormat(n: float):
    if n.is_integer():
        return int(n)
    return f'{n:.2f}'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
