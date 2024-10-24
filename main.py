from interface import *
from arithmetic import *
from sys import exit

author = 'Hitallo Azevedo'
version = 'v0.0.3'

# Github: @HitalloAzevedo

def App():
    while True:
        drawHeader([(True, f'MENU ESCOLAR {version}'), (False, f'Criado por {author}')])

        option = menu(
            'Progressão Aritmética',
            'Progressão Geométrica',
            'Fibonacci',
            'Função Primeiro Grau',
            'Função Segundo Grau',
            'Logaritmo',
            'Medidas de Dispersão',
            'SAIR'
        )

        if option == 99:
            print('Obrigado por usar!')
            input('Pressione ENTER para sair!')
            exit()
        
        match option:
            case 1:
                drawHeader([(True, 'Progressão Aritmética')])
                print('Informe o valor do primeiro termo: ', end='')
                a1 = getRealNumber()
                print('Informe o valor da razão: ', end='')
                r = getRealNumber()
                print('Informe o N-ésimo termo: ', end='')
                n = getIntegerNumber()

                pa = ArithmeticProgression(a1, r)
                paResults = pa.getSequence(n)

                drawHeader([(True, 'Resultados')], clearTerminal=False)
                showSequence(paResults[1])
                print('Soma da sequência: ', integerFormat(paResults[0]))
                print(f'N-ésimo termo ({n}): ', integerFormat(pa.getTermValue(n)))

                input('\n<< pressione enter para retornar ao menu >>')

            case 2:
                drawHeader([(True, 'Progressão Geométrica')])
                print('Informe o valor do primeiro termo: ', end='')
                a1 = getRealNumber()
                print('Informe o valor da razão: ', end='')
                r = getRealNumber()
                print('Informe o N-ésimo termo: ', end='')
                n = getIntegerNumber()

                pg = GeometricProgression(a1, r)
                pgResults = pg.getSequence(n)

                drawHeader([(True, 'Resultados')], clearTerminal=False)
                showSequence(pgResults[1])
                print('Soma da sequência: ', integerFormat(pgResults[0]))
                print(f'N-ésimo termo ({n}): ', integerFormat(pg.getTermValue(n)))

                input('\n<< pressione enter para retornar ao menu >>')

            case 3:
                drawHeader([(True, 'Fibonacci')], clearTerminal=True)
                print('Informe o N-ésimo termo da sequência: ', end='')
                n = getIntegerNumber()

                fib = Fibonacci(n)
                fibResults = fib.getFibonacciSequence()

                drawHeader([(True, 'Resultados')], clearTerminal=False)
                showSequence(fibResults[1])
                print('Soma dos termos: ', fibResults[0])
                print(f'N-ésimo termo ({n}): ', fib.getFibonacciTerm())

                input('\n<< pressione enter para retornar ao menu >>')

            case 4:
                drawHeader([(True, 'Função do Primeiro Grau')])
                print('Informe o valor de (A): ', end='')
                a = getRealNumber()
                print('Informe o valor de (X): ', end='')
                x = getRealNumber()
                print('Informe o valor de (B): ', end='')
                b = getRealNumber()

                affineFunction = AffineFunction(a, x, b)
                
                drawHeader([(True, 'Resultados')], clearTerminal=False)
                print(f'f({integerFormat(x)}) = {integerFormat(affineFunction.evalY())}')
                print(f'f(0) = y = {integerFormat(affineFunction.evalIntersectionY())}')
                print(f'Coordenadas: (0, {integerFormat(affineFunction.evalIntersectionY())}) e ({integerFormat(affineFunction.evalRoot())}, 0)')
                print(f'A reta da função é {affineFunction.getSlope()}')

                input('\n<< pressione enter para retornar ao menu >>')

            case 5:
                drawHeader([(True, 'Função do Segundo Grau')])
                print('Informe o valor de (A): ', end='')
                a = getRealNumber()
                print('Informe o valor de (B): ', end='')
                b = getRealNumber()
                print('Informe o valor de (C): ', end='')
                c = getRealNumber()

                quadraticFunction = QuadraticFunction(a, b, c)
                
                drawHeader([(True, 'Resultados')], clearTerminal=False)
                print(f'Δ: {integerFormat(quadraticFunction.evalDelta())}')
                print(
                    f'Raízes reais (Xi, Xii): ({integerFormat(quadraticFunction.bhaskara()[0])}, {integerFormat(quadraticFunction.bhaskara()[1])})' 
                    if quadraticFunction.bhaskara() 
                    else 'Não possui raízes reais'
                )
                print(f'Concavidade do gráfico para {quadraticFunction.returnConcavity()}')
                print(f'Vértice da parábola (x, y): ({integerFormat(quadraticFunction.evalVertexX())}, {integerFormat(quadraticFunction.evalVertexY())})')

                input('\n<< pressione enter para retornar ao menu >>')
            
            case 6:
                drawHeader([(True, 'Logaritmo')])
                print('Informe o valor da (base): ', end='')
                base = getRealNumber()
                print('Informe o valor de (N): ', end='')
                n = getRealNumber()

                log = Logarithm(n, base)
                
                drawHeader([(True, 'Resultados')], clearTerminal=False)
                print(f'Log de {integerFormat(n)} na base {integerFormat(base)} é {integerFormat(log.getLogarithm())}')

                input('\n<< pressione enter para retornar ao menu >>')
            
            case 7:
                drawHeader([(True, 'Dispersão')])
                print('Informa os valores separados por espaço. Ex: 1 2 3')
                print('>>> ', end='')
                numbers = list()
                [numbers.append(float(i)) for i in input().strip().split(' ')]

                dispersion = Dispersion(numbers)

                print('Média:', dispersion.average())
                print('Amplitude:', dispersion.spread())
                print('Desvio:', dispersion.deviation())
                print('Desvio Absoluto:', dispersion.absolute_deviation())
                print('Desvio Médio Absoluto:', dispersion.absolute_mean_deviation())
                print('Variância', dispersion.variance())
                print('Desvio Padrão', dispersion.standard_deviation())
                print('Variância Viciada:',dispersion.biased_variance())
                print('Desvio padrão Viciado:', dispersion.biased_standard_deviation())
                
                input('\n<< pressione enter para retornar ao menu >>')
            
            case _:
                pass

if __name__ == '__main__':
    App()
