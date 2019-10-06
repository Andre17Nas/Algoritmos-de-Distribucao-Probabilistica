import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array(range(25, 69, 1))
#BINOMIAL
'''
n = numero de vezes que a tentativa é repetida
P = probabilidade de sucesso em uma tentativa unica
Q = a probabilidade de fracasso em  uma tentativa unica (Q = 1 - P)
x = a variavel aleatoria representa a contagem dos numeros de sucessos nas tentativas : x = 0,1,2,3, ..., n


b = (n!/(n-x)!*(n!) * (P ** x) * (Q ** (n-x))
'''

numero_tentativas = 5
P = 1/np.alen(x)
Q = 1 - P
x_var = np.random.choice(5)
print(x_var)

#b = (math.factorial(numero_tentativas)/(math.factorial(numero_tentativas - x_var))) *((P ** x) * (Q ** (numero_tentativas - x_var)))
b = (math.factorial(numero_tentativas)/(math.factorial(numero_tentativas - x_var))) *(np.power(P, x) * np.power(Q, (numero_tentativas - x_var)))

print("binomial", b)
plt.plot(x, b)
plt.grid(True)
plt.title('distributiva probabilitica binomial')
plt.show()