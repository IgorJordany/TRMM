import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres
from math import sqrt

# Conectando no banco

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='qwe123@ic')

# Lendo os dados

cur = con.cursor()
cur.execute("SELECT bruto FROM anual where id = 4") # Select no banco
rows = cur.fetchall()
for row in rows:
	A = np.array(row[0],dtype=float) # Recuperando string do banco para numpyarray float

cur.execute("SELECT bruto FROM anual where id = 9") # Select no banco
rows = cur.fetchall()
for row in rows:
	B = np.array(row[0],dtype=float) # Recuperando string do banco para numpyarray float

#Calcula distancia Euclidiana
soma = 0
for i in range(360):
	soma = soma + ((A[i]-B[i])**2)
dist= sqrt(soma)

print dist
# Make the changes to the database persistent
con.commit()
# Close communication with the database
cur.close()
con.close()