# -*- coding: utf-8 -*-
import sympy as sp
from sympy.plotting import plot
from sympy import Symbol, S
from sympy import init_printing
from sympy import integrate, Symbol, dsolve, Function, diff, Eq, roots
from sympy.calculus.util import continuous_domain
import matplotlib.pyplot as plt
import math
import warnings
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='White', backcolor='Black', fontsize=10)
warnings.filterwarnings("ignore")
pi = math.pi
x = sp.symbols('x')
line = '-' * 70 


def raizes_funcao(funcao):
    raizes_reais = []
    raizes_imaginarias = []
    
    raizes = sp.solve(funcao)
    n_raizes = len(raizes)

    for i in range(n_raizes):
         try:
            float(raizes[i])
            k = float(raizes[i])
            raizes_reais.append(k)
      #     print('raiz real' , k)
         except:
             k = complex(raizes[i])
             raizes_imaginarias.append(k)
       #     print('raiz imaginaria' , k)
        
    if len(raizes) == 0:
        print('A função não possui raízes')
    elif len(raizes_reais) == 0 and len(raizes_imaginarias) > 0:
        print('A função não possui raízes reais')
        print('raizes imaginárias:' , raizes_imaginarias)
    elif len(raizes_imaginarias) == 0 and len(raizes_reais) > 0:  
        print('raizes reais:' , raizes_reais)
    else:
        print('raizes reais:' , raizes_reais)
        print('raizes imaginárias:' , raizes_imaginarias)


# Definir a função:
print(line)

funcao = 

print('f(x) =' , funcao)
#funcao = input('f(x) = ' , )
print('Domínio de f:' , continuous_domain(funcao, x, S.Reals))
plot(funcao, (x, -6, 6) , ylim=[-15,15] , line_color = 'blue')
raizes_funcao(funcao)
print(line)

# Integral Indefinida:
    
integral = integrate(funcao, x)
print('F(X) = ' , integral , '+ K')
print(line)

# Gráfico da função -> Família de antiderivadas
lims = {'xlim': (-5,5), 'ylim': (-4,10)}

px = plot(integral, show=False, **lims)
for k in range(-1,3):      # Constantes K
    y1 = integral + k
    px1 = plot(y1, show=False, **lims)
    px.extend(px1)
    
px.show()




