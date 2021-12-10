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
            PA()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    PA()

        elif opcao == 2:
            PG()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    PG()

        elif opcao == 3:
            fibonacci()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    fibonacci()

        elif opcao == 4:
            funcao_primeiro()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    funcao_primeiro()

        elif opcao == 5:
            funcao_segundo()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    funcao_segundo()

        elif opcao == 6:
            logaritmo()
            while True:
                r = resposta()
                if r == 'n':
                    main()
                else:
                    logaritmo()

if __name__ == '__main__':
    main()