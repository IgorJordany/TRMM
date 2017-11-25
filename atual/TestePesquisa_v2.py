import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres

# Conectando no banco

con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='postgres')

# Lendo os dados

cur = con.cursor()
cur.execute("SELECT bruto FROM anual where id = 1") # Select no banco
rows = cur.fetchall()
for row in rows:
	x = np.array(row[0],dtype=float) # Recuperando string do banco para numpyarray float
# Salvando a lista no banco

print(x)
# Make the changes to the database persistent
con.commit()
# Close communication with the database
cur.close()
con.close()