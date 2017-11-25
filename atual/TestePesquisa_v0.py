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
print(sst)
print(len(sst))

# Geracaoo de matriz para plot
variance = np.std(sst, ddof=1) ** 2
sst = (sst - np.mean(sst)) / np.std(sst, ddof=1)
print("\nDados tratados:")
print(sst)

#SELECT precipitac from trmm where lat = -22.125000000000000 and lon = -61.875000000000000 and datatrm = '1999/01/01';
#SELECT lat,lon,id FROM trmm WHERE lat = -22.125000000000000 and lon = -61.875000000000000 GROUP BY lat,lon, id;
#SELECT id,lat,lon FROM trmm GROUP BY id,lat,lon;nq