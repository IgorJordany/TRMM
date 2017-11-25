import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres

# Conectando no banco

con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='qwe123@ic')
cur = con.cursor()
# Lendo os dados
for i in range(2597): # Pegando os pontos separados
	cur.execute("SELECT * FROM ponto WHERE id = %s" %(i+1)) # Pegando dados da tabela ponto
	temp = cur.fetchall()
	for row in temp:
		ide = int(row[0]) # Convercao de tupla lida do banco para lista float
		lat = float(row[1])
		lon = float(row[2])
	print("Id ponto: %s" %(ide))
	print('Ano 1998 ate 2014')
	arquivo = [] # Lista
	cur.execute("SELECT precipitac FROM trmm where lat = %s and lon = %s and datatrmm >= '1998/01/01' and datatrmm <= '2014/01/01' order by datatrmm" %(lat,lon)) # Select no banco
	rows = cur.fetchall()
	for row in rows:
		arquivo.append(float(row[0])) # Convercao de tupla lida do banco para lista float
	sst = np.asarray(arquivo)  # Lista de dados tirados do banco
	print("Tamanho sst bruto: %s" %(len(sst)))
	bruto = ','.join(str(x) for x in sst) # Converte numpyarray em string pronta para entrar no banco.

	# Geracao de lista para plot
	variance = np.std(sst, ddof=1) ** 2
	sst = (sst - np.mean(sst)) / np.std(sst, ddof=1)

	print("Tamanho sst tratado: %s \n" %(len(sst)))
	tratado = ','.join(str(x) for x in sst) # converte numpyarray em string pronta para entrar no banco.

	# Salvando a lista no banco
	cur.execute("INSERT INTO total (cod_ponto, bruto, tratado) VALUES ('%s', '{%s}', '{%s}')" %(ide, bruto, tratado))

	# Make the changes to the database persistent
	con.commit()

# Close communication with the database
cur.close()
con.close()