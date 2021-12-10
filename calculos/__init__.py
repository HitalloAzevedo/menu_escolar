from interface import cabecalho, leiafloat, leiaint


def PG():
    cabecalho('PROGRESSÃO GEOMÉTRICA')
    a1 = leiafloat('Informe o primeiro termo: ')
    q = leiafloat('Informe a razão: ')
    qtd = leiaint('Até qual termo deseja visualizar?: ')

    for n in range(1, qtd + 1):
        tg = a1*q**(n-1)
        if tg.is_integer():
            tg = int(tg)
        else:
            tg = f'{tg:.2f}'
        print(tg, end=' -> ')
    
    print('Fim!')


def PA():
    pass


def funcao_primeiro():
    pass


def funcao_segundo():
    pass


def fibonacci():
    pass


def logaritmo():
    pass