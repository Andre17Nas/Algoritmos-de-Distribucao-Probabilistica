# DISTRIBUICAO DE PROBABILIDADE POISSON
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

x = np.array(range(25, 69, 1))
print(x)

# constants
e = 2.718
pi = 3.14

'''
x = numero de ocorrencias num dado intervalo
u = numero medio de ocorrendias dada uma determnada unidade de tempo e espcao
M =
e = 2.718

p = ((M ** x)/math.factorial(x))*desvio_padrao**(-x)
'''

numero_medio_ocorrencias_tempo = 5 # x
numero_de_ocorrencias_intervalo = x # u

# poisson = u^x * e ^(-u)/x!

#poisson = ((numero_medio_ocorrencias_tempo ** numero_de_ocorrencias_intervalo)* (e **(- numero_medio_ocorrencias_tempo)))/math.factorial(numero_medio_ocorrencias_tempo)
p = np.power(numero_medio_ocorrencias_tempo, numero_de_ocorrencias_intervalo) * np.power(e, (- numero_medio_ocorrencias_tempo)/math.factorial(numero_medio_ocorrencias_tempo))
print("Distribuicao de probabilidade Poisson", p)

plt.plot(p)
plt.grid(True)
plt.title('Distribuicao de probabilidade Poisson')
plt.show()