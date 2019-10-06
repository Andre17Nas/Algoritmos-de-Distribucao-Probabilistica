import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

# Costantes
'''
err0 => e
pi => pi
'''
e = 2.718
pi = 3.14

# array idade á altura(cm)
x = np.array(range(25, 69, 1))

plt.plot(x)
plt.grid(True)
plt.title('O Gráfico do vetor entre entre a idade 25 e a altura em cm 68: ')
plt.show()

# media, mediana, desvio_p
media = np.mean(x)
mediana = np.median(x)
moda = stats.mode(x)
desvio_padrao = np.std(x)
varianca = desvio_padrao * desvio_padrao

# tem um numero finito de possiveis resultados, numeros inteiros
#var_aleatoria_discreta = np.random.choice(x)

# Qual a chance de encontrar a média como variavel aleatoria continua?
var_aleatoria_continua = np.linspace(25, 68, 44)


# DISTRIBUICAO DE PROBABILIDADE NORMAL
y = (1 / desvio_padrao*(np.sqrt(2 * pi))) * np.power(e, (-(var_aleatoria_continua - media) ** 2) / (2 * varianca))


print(y)
plt.plot(x, y) #plt.plot( x, y )
plt.grid(True)
plt.title('Distribuição de probabilidade normal')
plt.show()


# ................................................................................................................................................................

