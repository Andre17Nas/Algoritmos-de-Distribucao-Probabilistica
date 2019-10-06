# DISTRIBUICAO PROBABILITICA UNIFORME
import numpy as np
import matplotlib.pyplot as plt

# Vetor em questao
x = np.array(range(25, 68, 1))

a = 20
b = 40

# A variavel que estou procurando dentro do vetor
var_ale_continua = 30.32

'''
if x >= 30 and x <= 40:
    y = 1/(b - a)
elif x < 30 and x > 40:
    y = 0

'''
ya = 1/(b - a)

#yb = np.random.uniform(25, 68)


plt.hist(ya)
plt.ylabel('f(x) = 1/b-a')
plt.grid(True)
plt.title('Distribuicao de probabilidade Uniforme')
plt.show()