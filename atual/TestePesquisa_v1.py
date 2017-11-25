import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres

# Conectando no banco

con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='postgres')

# Lendo os dados

arquivo = [] # Lista
cur = con.cursor()
cur.execute("SELECT precipitac FROM trmm where lat = -22.125000000000000 and lon = -61.875000000000000 and datatrmm >= '1998/01/01' and datatrmm <= '1999/01/01' order by datatrmm limit 360") # Select no banco
rows = cur.fetchall()
for row in rows:
	arquivo.append(float(row[0])) # Convercao de tupla lida do banco para lista float
sst = np.asarray(arquivo)  # Lista de dados tirados do banco

teste = ','.join(str(x) for x in sst) # Converte numpyarray em string pronta para entrar no banco.

# Geracao de lista para plot
variance = np.std(sst, ddof=1) ** 2
sst = (sst - np.mean(sst)) / np.std(sst, ddof=1)
print("\nDados tratados:")

# Salvando a lista no banco
cur.execute("INSERT INTO teste VALUES('{%s}')"%(teste))

# Make the changes to the database persistent
con.commit()

# Close communication with the database
cur.close()
con.close()