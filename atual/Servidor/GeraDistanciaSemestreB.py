#encoding: utf-8
import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
from math import sqrt
from datetime import datetime

# Conectando no banco
log=open('dist_semestre_inicioB.txt','w')
data = datetime.now()
log.write("data: "+str(data.day)+" / "+str(data.month)+" / "+str(data.year)+"\n"+"tempo: "+str(data.hour)+":"+str(data.minute)+":"+str(data.second))
log.close()

con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='qwe123@ic')
cur = con.cursor()
# Lendo os dados
for i in range(1,83105):
	lista=[]
	cur.execute("SELECT * FROM semestral where id = %s" %(i)) # Select no banco
	rows1 = cur.fetchall()
	for row1 in rows1: # Obtendo dados do banco de dados e convertendo em formato utilizavel
		Aid = int(row1[0])
		Acod_ponto = int(row1[1])
		ABruto = np.array(row1[2],dtype=float)
		AWavelet = np.array(row1[3],dtype=float)
		Adata = np.array(row1[4],dtype=str)
	for j in range(1,83105):
		cur.execute("SELECT * FROM semestral where id = %s" %(j)) # Select no banco
		rows2 = cur.fetchall()
		for row2 in rows2: # Obtendo dados do banco de dados e convertendo em formato utilizavel
			Bid = int(row2[0])
			Bcod_ponto = int(row2[1])
			BBruto = np.array(row2[2],dtype=float)
			BWavelet = np.array(row2[3],dtype=float)
			Bdata = np.array(row2[4],dtype=str)
		if Acod_ponto != Bcod_ponto and Adata != Bdata:
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
			aux=(distBruto, distWavelet, Bcod_ponto, Bdata)
			lista.append(aux)
	lista.sort()
	lista6primeiros=[]
	for linha in lista[0:6]:
		distOrdw = linha[1]
		distOrdb = linha[0]
		codPontob = linha[2]
		dataB = linha[3]
		lista6primeiros.append(codPontob)  	#0	4	8	12	16	20
		lista6primeiros.append(distOrdb)	#1	5	9	13	17	21
		lista6primeiros.append(distOrdw)	#2	6	10	14	18	22
		lista6primeiros.append(dataB)		#3	7	11	15	19	23
	cur.execute("INSERT INTO distsemestreB (codPonto, datPonto, codPonto1, distBruta1, distTratada1, datPonto1, codPonto2, distBruta2, distTratada2, datPonto2, codPonto3, distBruta3, distTratada3, datPonto3, codPonto4, distBruta4, distTratada4, datPonto4, codPonto5, distBruta5, distTratada5, datPonto5, codPonto6, distBruta6, distTratada6, datPonto6) VALUES('%s','%s','%s','{%s}','{%s}','%s','%s','{%s}','{%s}','%s','%s','{%s}','{%s}','%s','%s','{%s}','{%s}','%s','%s','{%s}','{%s}','%s','%s','{%s}','{%s}','%s')"%(Acod_ponto,Adata,lista6primeiros[0],lista6primeiros[1],lista6primeiros[2],lista6primeiros[3],lista6primeiros[4],lista6primeiros[5],lista6primeiros[6],lista6primeiros[7],lista6primeiros[8],lista6primeiros[9],lista6primeiros[10],lista6primeiros[11],lista6primeiros[12],lista6primeiros[13],lista6primeiros[14],lista6primeiros[15],lista6primeiros[16],lista6primeiros[17],lista6primeiros[18],lista6primeiros[19],lista6primeiros[20],lista6primeiros[21],lista6primeiros[22],lista6primeiros[23]))
	con.commit()
# Make the changes to the database persistent
con.commit()
# Fechar comunicacao com o banco
cur.close()
con.close()

log=open('dist_semestre_terminoB.txt','w')
data = datetime.now()
log.write("data: "+str(data.day)+" / "+str(data.month)+" / "+str(data.year)+"\n"+"tempo: "+str(data.hour)+":"+str(data.minute)+":"+str(data.second))
log.close()