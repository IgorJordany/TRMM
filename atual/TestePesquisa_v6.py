import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres
from math import sqrt

# Conectando no banco

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='qwe123@ic')
cur = con.cursor()

lista=[]
for i in range(1,83073):
	cur.execute("SELECT * FROM aux where id = %s"%(i)) # Select no banco
	rows1 = cur.fetchall()
	for row1 in rows1: # Obtendo dados do banco de dados e convertendo em formato utilizavel
		ids = int(row1[0])
		codPontoA = int(row1[1])
		codPontoB = int(row1[2])
		distBruto = np.array(row1[3],dtype=float)
		distWavelet = np.array(row1[4],dtype=float)
		dataa = np.array(row1[5],dtype=str)
		datab = np.array(row1[6],dtype=str)
	if dataa != datab:
		aux=(float(distWavelet[0]),ids,codPontoA,codPontoB)
		lista.append(aux)
lista.sort()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])

'''lista=[]
lista=[(3,1),(2,2),(6,3),(1,4),(5,5),(-3,6)]
aux=(-2,7)
print(lista)
lista.append(aux)
lista.sort()
print(lista)'''

con.commit()
# Fechar comunicacao com o banco
cur.close()
con.close()