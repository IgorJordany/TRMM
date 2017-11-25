# programa graficos.py
# coding: utf-8


import matplotlib.pyplot as plt

import numpy as np 


f = lambda t: np.exp(-t) * np.cos(2*np.pi*t) 


t1 = np.linspace(5,10,num=100) 

yt1 = f(t1)

t2 = np.linspace(5,25,num=100) 

yt2 = f(t2)


plt.figure(1)      # Cria a janela

plt.subplot(2,1,1) # Cria a área do primeiro gráfico

plt.plot(t1, yt1, 'bo', t2, yt2, 'k') # Desenha o gráfico


plt.subplot(2,1,2)   # Cria a área do segundo gráfico

ycos = np.cos(2*np.pi*t2)


plt.plot(t2, ycos, 'r--')  # Desenha o segundo gráfico

plt.savefig('teste.png')
plt.show()
