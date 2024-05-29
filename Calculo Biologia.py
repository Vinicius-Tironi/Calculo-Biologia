# -*- coding: utf-8 -*-

import sympy as sp
from sympy.plotting import plot
from sympy import Symbol, S
from sympy.calculus.util import continuous_domain
import math
import warnings
warnings.filterwarnings("ignore")
pi = math.pi
x = sp.symbols('x')
line = '-' * 70
print(line)


def raizes_funcao(funcao):
    zeros = []
    dominio = continuous_domain(funcao, x, S.Reals)
    for p in map(lambda x: x/10.0, range(-300, 301, 1)):
        fp = funcao.subs(x, p)
        #print('f(' , p , ')= ' , fp)
        if p in dominio and fp == 0:
            zeros.append(p)
    if bool(zeros) == False:
        print('A função não possui raízes.')
    else:
        print('Raízes: x =' , zeros)    



# Definir a função

funcao = x

print('f(x) =' , funcao)
#funcao = input('f(x) = ' , )
print('Domínio de f:' , continuous_domain(funcao, x, S.Reals))
plot(funcao, (x, -6, 6) , ylim=[-15,15] , line_color = 'blue')
raizes_funcao(funcao)
print(line)


# Primeira derivada
primeira_derivada = sp.diff(funcao, x)
print('f′(x) = ' , primeira_derivada)
print('Domínio de f′:' , continuous_domain(primeira_derivada, x, S.Reals))
plot(primeira_derivada, (x, -6, 6), ylim=[-15,15] , line_color = 'green')
raizes_funcao(primeira_derivada)
print(line)


# Segunda derivada
segunda_derivada = sp.diff(primeira_derivada, x)
print('f′′(x) = ' , segunda_derivada)
print('Domínio de f′′:' , continuous_domain(segunda_derivada, x, S.Reals))
plot(segunda_derivada, (x, -6, 6), ylim=[-15,15] , line_color = 'red')
raizes_funcao(segunda_derivada)
print(line)


