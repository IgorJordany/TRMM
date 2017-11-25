#encoding: utf-8
import numpy as np
from waveletFunctions import wavelet, wave_signif
from mpl_toolkits.axes_grid1 import make_axes_locatable
import psycopg2 #Importando biblioteca que comunica com o postgres
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
from math import sqrt

# Conectando no banco

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='qwe123@ic')
cur = con.cursor()
cur.execute("CREATE TABLE aux (id serial PRIMARY KEY, cod_pontoA integer, cod_pontoB integer, distanciaBruto float, distanciaTratado float , dataA BYTEA , dataB BYTEA, FOREIGN KEY (cod_pontoA) REFERENCES ponto, FOREIGN KEY (cod_pontoB) REFERENCES ponto)")
cur.execute("drop table aux")
cur.execute("drop table test")
con.commit()
# Fechar comunicacao com o banco
cur.close()
con.close()