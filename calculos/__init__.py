from interface import cabecalho, leiafloat, leiaint


def PG():
    cabecalho('PROGRESSÃO GEOMÉTRICA')

    a1 = leiafloat('Informe o primeiro termo: ')
    q = leiafloat('Informe a razão: ')
    qtd = leiaint('Até qual termo deseja visualizar?: ')

    soma = 0

    for n in range(1, qtd + 1):
        tg = a1*q**(n-1)
        if tg.is_integer():
            tg = int(tg)
        else:
            tg = f'{tg:.2f}'
        print(tg, end=' -> ')
        soma += tg
    
    print('FIM!')
    print(f'A soma de todos os termos: {soma}')


def PA():
    cabecalho('PROGRESSÃO ARITIMÉTICA')

    a1 = leiafloat('Informe o primeiro termo: ')
    q = leiafloat('Informe a razão: ')
    qtd = leiaint('Até qual termo deseja visualizar?: ')

    soma = 0

    for n in range(1, qtd+1):
        tg = a1+(n-1)*q
        if tg.is_integer():
            tg = int(tg)
        else:
            tg = f'{tg:.2f}'
        print(tg, end=' -> ')
        soma += tg
    
    print('FIM!')
    print(f'A soma de todos os termos: {soma}')


def funcao_primeiro():
    pass


def funcao_segundo():
    pass


def fibonacci():
    pass


def logaritmo():
    pass