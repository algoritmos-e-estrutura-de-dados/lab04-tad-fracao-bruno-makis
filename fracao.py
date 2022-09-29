import math
class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    #soma
    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (fracao.numerador*self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)
   
    #subtração
    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    #multiplicação
    def multi (self, fracao):
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    #simplificação
    def simplify (self,fracao):
        div = math.gcd(fracao.numerador , fracao.denominador)
        return f"{fracao.numerador/div}/{fracao.denominador/div}"

    #fração
    def solve(self, fracao):
        return (self.numerador)/(self.denominador)

    #frac
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

#atribui
fracao1 = Fracao(7, 5)
fracao2 = Fracao(6, 4)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.multi(fracao2)
fracao6 = fracao1.simplify(fracao2)

#mostra
print(f"fracao1:{fracao1}")
print(f"fracao2:{fracao2}")
print(f"fracao3:{fracao3}")
print(f"fracao4:{fracao4}")
print(f"fracao5:{fracao5}")
print(f"fracao6:{fracao6}")
