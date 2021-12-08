def menu(*opcoes):
    c = 1
    for o in opcoes:
        print(f'{c} - {o}')
        c += 1
    
    opcao = leiaint('Informe sua opção: ')
    return opcao

def cabecalho(msg:str, tam=60, simb='='):
    print(simb * tam)
    print(msg.center(tam))
    print(simb * tam)


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor insira um valor inteiro!') 
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor insira um valor inteiro!') 
        else:
            return valor

