import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2
from datetime import datetime

# Conectando no banco

con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='qwe123@ic')
cur = con.cursor()

cur.execute("SELECT bruto FROM totalMatriz where id=2") # Select no banco
SB = cur.fetchall()

'''
log=open('LTI.txt','w')
data = datetime.now()
log.write("data: "+str(data.day)+" / "+str(data.month)+" / "+str(data.year)+"\n"+"tempo: "+str(data.hour)+":"+str(data.minute)+":"+str(data.second))
log.close()
'''
Bruto=[]
#Wavelet=[]
#MatB=np.zeros((40,40))
#MatW=np.zeros((40,40))
for i in SB:
	Bruto.append(i[0])
	#Wavelet.append(i[1])

print(len(Bruto))
fon = np.array(Bruto)
print(len(fon.flat[:]))
'''
for PA in range(0,40):
	for PB in range(PA,40):

		PBA = np.array(Bruto[PA])
		PBB = np.array(Bruto[PB])

		PWA = np.array(Wavelet[PA])
		PWB = np.array(Wavelet[PB])

		DistB = np.linalg.norm(PBA-PBB)
		DistW = np.linalg.norm(PWA-PWB)

		MatB[PA][PB] = DistB
		MatW[PA][PB] = DistW

MDB = MatB.transpose() + MatB
MDB = MDB.flat[:]
MDW = MatW.transpose() + MatW
MDW = MDW.flat[:]

BMDB = ','.join(str(x) for x in MDB)
BMDW = ','.join(str(x) for x in MDW)
cur.execute("INSERT INTO totalMatriz (bruto,wavelet) values('{%s}','{%s}')"%(BMDB, BMDW))
con.commit()

log=open('LTF.txt','w')
data = datetime.now()
log.write("data: "+str(data.day)+" / "+str(data.month)+" / "+str(data.year)+"\n"+"tempo: "+str(data.hour)+":"+str(data.minute)+":"+str(data.second))
log.close()
'''
cur.close()
con.close()

'''
Documentacao variaveis:
SB 		= Select Banco
MatB 	= Matriz dados Brutos
MatW	= Matriz dados Wavelet

PA 		= Ponto A
PBA 	= Ponto Bruto A
PWA 	= Ponto Wavelet A

PB 		= Ponto B
PBB 	= Ponto Bruto B
PWB 	= Ponto Wavelet B

DistB 	= Distancia Euclidiana Bruta
DistW 	= Distancia Euclidiana Wavelet

MDB 	= Matriz Distancia Bruta
MDW 	= Matriz Distancia Wavelet

BMDB 	= Banco Matriz Distancia Bruta
BMDW 	= Banco Matriz Distancia Wavelet

Arquivos log:

LTI 	= Log Teste Inicial
LTF 	= Log Teste Final
'''