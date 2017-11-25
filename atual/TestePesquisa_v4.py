import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres
from math import sqrt

# Conectando no banco

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='qwe123@ic')
cur = con.cursor()
# Lendo os dados
for i in range(1,3):
	cur.execute("SELECT * FROM semestral where id = %s" %(i)) # Select no banco
	rows1 = cur.fetchall()
	for row1 in rows1: # Obtendo dados do banco de dados e convertendo em formato utilizavel
		Aid = int(row1[0])
		Acod_ponto = int(row1[1])
		ABruto = np.array(row1[2],dtype=float)
		AWavelet = np.array(row1[3],dtype=float)
		Adata = np.array(row1[4],dtype=str)
	for j in range(i,40):
		cur.execute("SELECT * FROM semestral where id = %s" %(j)) # Select no banco
		rows2 = cur.fetchall()
		for row2 in rows2: # Obtendo dados do banco de dados e convertendo em formato utilizavel
			Bid = np.array(row2[0],dtype=int)
			Bcod_ponto = np.array(row2[1],dtype=int)
			BBruto = np.array(row2[2],dtype=float)
			BWavelet = np.array(row2[3],dtype=float)
			Bdata = np.array(row2[4],dtype=str)
		if Acod_ponto != Bcod_ponto:
			soma1 = 0 #Calcula distancia Euclidiana
			soma2 = 0
			for i in range(180):
				soma1 = soma1 + ((ABruto[i]-BBruto[i])**2)
				soma2 = soma2 + ((AWavelet[i]-BWavelet[i])**2)
			distBruto= sqrt(soma1)
			distWavelet = sqrt(soma2)
			print("Pontos sendo calculados: %s e %s" %(Acod_ponto,Bcod_ponto))
			print("Resultado distancia Bruta: %s" %(distBruto))
			print("Resultado distancia Wavelet: %s" %(distWavelet))
			print("Data do ponto A = %s / ponto B = %s \n" %(Adata,Bdata))
			cur.execute("INSERT INTO distanciaSemestre (cod_pontoa, cod_pontob, distanciabruto, distanciatratado, dataa, datab) VALUES ('%s','%s','{%s}','{%s}','%s','%s')" %(Acod_ponto, Bcod_ponto, distBruto, distWavelet, Adata, Bdata))

# Make the changes to the database persistent
con.commit()
# Fechar comunicacao com o banco
cur.close()
con.close()