from math import log
from interface import *
from calculos import *

author = 'Hitallo Azevedo'
version = 'v0.0.1'

# Muito obrigado pela preferência Github: @HitalloAzevedo

def main():
    while True:
        cabecalho(f'MENU ESCOLAR {version}')
        print(f'Criado por {author}')
        print('=' * 60)

        opcao = menu('Progressão Aritmética',
        'Progressão Geométrica',
        'Fibonacci',
        'Função Primeiro Grau',
        'Função Segundo Grau',
        'Logaritmo')

        if opcao == 99:
            print('Obrigado por usar!')
            exit()

        elif opcao == 1:
            limpar()
            PA()
            while True:
                r = resposta()
                if r == 'n':
                    limpar()
                    main()
                else:
                    limpar()
                    PA()

        elif opcao == 2:
            limpar()
            PG()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    limpar()
                    PG()

        elif opcao == 3:
            limpar()
            fibonacci()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    limpar()
                    fibonacci()

        elif opcao == 4:
            limpar()
            funcao_primeiro()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    limpar()
                    funcao_primeiro()

        elif opcao == 5:
            limpar()
            funcao_segundo()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    limpar()
                    funcao_segundo()

        elif opcao == 6:
            limpar()
            logaritmo()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    limpar()
                    logaritmo()

if __name__ == '__main__':
    main()