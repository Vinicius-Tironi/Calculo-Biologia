# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
pi = math.pi


# Definir a Função

f = lambda x : (np.sin(4*x))

a = -pi ; b = pi ;  N = 100
n = 10

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.figure(figsize=(10, 5))

plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Soma de Riemman, N = {}'.format(N))

plt.show()

dx = (b-a)/N
x_midpoint = np.linspace(dx/2,b - dx/2,N)

print("Partição com",N,"subintervalos.")

midpoint_riemann_sum = np.sum(f(x_mid) * dx)      # Soma de Riemann
if midpoint_riemann_sum < 10**-12:
    midpoint_riemann_sum = 0
print("Soma de Riemman:",midpoint_riemann_sum)

def integral_exata(funcao):    # Valor exato da integral
    Quad = quad(funcao,a,b)
    I = Quad[0]
  # E = Quad[1]
    print('Valor exato = ' , I)
  # print('Erro do cálculo =' , E)
    
    return I

I = integral_exata(f)


print("Erro:",np.abs(midpoint_riemann_sum - I))