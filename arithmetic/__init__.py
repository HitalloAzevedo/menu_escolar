class QuadraticFunction:
    def __init__(self, a: float, b: float, c: float): 
        self.a = a
        self.b = b
        self.c = c
    
    def evalDelta(self):
        return self.b**2 - 4 * self.a * self.c
    
    def returnConcavity(self):
        if self.a > 0:
            return 'cima'
        elif self.a < 0:
            return 'baixo'
    
    def evalVertexY(self):
        return -self.evalDelta() / (4 * self.a)

    def evalVertexX(self):
        return -self.b / (2 * self.a)
    
    def bhaskara(self):
        from math import sqrt
        delta = self.evalDelta()
        if delta < 0:
            return False
        xi = (-self.b + sqrt(delta)) / (2 * self.a)
        xii = (-self.b - sqrt(delta)) / (2 * self.a)
        return (xi, xii)
    
class AffineFunction():
    def __init__(self, a: float, x: float, b: float):
        self.a = a
        self.x = x
        self.b = b

    def evalY(self):
        return self.a * self.x + self.b
    
    def evalRoot(self):
        return -self.b / self.a
    
    def evalIntersectionY(self):
        return self.b
    
    def getSlope(self):
        if self.a == 0:
            return 'constante'
        if self.a > 0:
            return 'crescente'
        if self.a < 0:
            return 'decrescente'
    
class Logarithm():
    def __init__(self, x: float, base: float):
        self.x = x
        self.base = base
    
    def getLogarithm(self):
        from math import log
        return log(self.x, self.base)
    
class Fibonacci():
    def __init__(self, terms: int):
        self.terms = terms

    def getFibonacciSequence(self):
        t1, t2 = 1, 1
        sequence = [t1, t2]
        if self.terms == 0:
            return [0]
        elif self.terms == 1:
            return [1]
        elif self.terms == 2:
            return sequence
        else:
            i = 0
            while (i < self.terms - 2):
                t3 = t1 + t2
                sequence.append(t3)
                t1 = t2
                t2 = t3
                i+=1

            return (sum(sequence), sequence)
        
    def getFibonacciTerm(self):
        return self.getFibonacciSequence()[1][self.terms - 1]

class GeometricProgression():
    def __init__(self, a1: float, r: float):
        self.a1 = a1
        self.r = r

    def getSequence(self, size):
        sequence = []
        for i in range(1, size + 1):
            sequence.append(self.getTermValue(i))
        return (sum(sequence), sequence)

    def getTermValue(self, index):
        return self.a1 * self.r**(index - 1)

class ArithmeticProgression():
    def __init__(self, a1: float, r: float):
        self.a1 = a1
        self.r = r
    
    def getSequence(self, size):
        sequence = []
        for i in range(1, size + 1):
            sequence.append(self.getTermValue(i))
        return (sum(sequence), sequence)

    def getTermValue(self, index):
        return self.a1 + (index - 1) * self.r

