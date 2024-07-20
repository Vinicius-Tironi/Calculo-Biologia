# -*- coding: utf-8 -*-
import sympy as sp
from sympy.plotting import plot
from sympy import Symbol, S
from sympy import init_printing
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='White', backcolor='Black', fontsize=10)
from sympy.calculus.util import continuous_domain
import math
import warnings
warnings.filterwarnings("ignore")
pi = math.pi
x = sp.symbols('x')
line = '-' * 70
print(line)


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


def grafico(funcao):  # Funciona bem para polinômios
    xmin = -5
    xmax = 5
    
    dominio = continuous_domain(funcao, x, S.Reals)
    descontinuidades = []
    for i in range(-100 , 100):  # Descontinuidades locais
        if i not in dominio:
            descontinuidades.append(i)
    if len(descontinuidades) < 20:
        print('descontinuidades:' , descontinuidades)
    
    if len(descontinuidades) == 1:
        a = descontinuidades[0]

        p1 = plot(funcao, (x, xmin, a)  , ylim=[-10,10] , line_color = 'blue', show=False)
        p2 = plot(funcao, (x, a, xmax)  , ylim=[-10,10] , line_color = 'blue' , show=False)
        
        p1.extend(p2)
        p1.show()
    elif len(descontinuidades) == 2:
        n = len(descontinuidades)
        
        p1 = plot(funcao, (x, xmin, descontinuidades[n-2])  , ylim=[-10,10] , line_color = 'blue', show=False)
        p2 = plot(funcao, (x, descontinuidades[n-2], descontinuidades[n-1])  , ylim=[-15,15] , line_color = 'blue' , show=False)
        p3 = plot(funcao, (x, descontinuidades[n-1], xmax)  , ylim=[-10,10] , line_color = 'blue', show=False)
        
        p1.extend(p2)
        p1.extend(p3)
        p1.show()

    elif len(descontinuidades) > 2 and len(descontinuidades) < 20:
        n = len(descontinuidades)
        n_plots = {}

        p0 = plot(funcao, (x, xmin, descontinuidades[0])  , ylim=[-10,10] , line_color = 'blue', show=False)
        for i in range(0, n-1):
            n_plots['plot_' + str(i+1)] = plot(funcao, (x, descontinuidades[i], descontinuidades[i+1])  , ylim=[-15,15] , line_color = 'blue' , show=False)
            locals().update(n_plots)
            p0.extend(n_plots['plot_' + str(i+1)])                    
        
        pn = plot(funcao, (x, descontinuidades[n-1], xmax)  , ylim=[-10,10] , line_color = 'blue' , show=False)    
        p0.extend(pn)
        p0.show()

        
    else:
        plot(funcao, (x, xmin, xmax), line_color = 'blue' , show = True)        



# Definir a função

funcao = sp.log(x)

print('f(x) =' , funcao)
#funcao = input('f(x) = ' , )
print('Domínio de f:' , continuous_domain(funcao, x, S.Reals))
raizes_funcao(funcao)
grafico(funcao)
print(line)


# Primeira derivada
primeira_derivada = sp.diff(funcao, x)
print('f′(x) = ' , primeira_derivada)
print('Domínio de f′:' , continuous_domain(primeira_derivada, x, S.Reals))
raizes_funcao(primeira_derivada)
grafico(primeira_derivada)
print(line)


# Segunda derivada
segunda_derivada = sp.diff(primeira_derivada, x)
print('f′′(x) = ' , segunda_derivada)
print('Domínio de f′′:' , continuous_domain(segunda_derivada, x, S.Reals))
raizes_funcao(segunda_derivada)
grafico(segunda_derivada)
print(line)