import psycopg2
con = psycopg2.connect(host='localhost', database='pesquisa', user='postgres', password='postgres')
cur = con.cursor()
cur.execute("SELECT id,lat,lon FROM trmm GROUP BY id,lat,lon;")
arq = open('tab.txt','w')
rows = cur.fetchall()
for row in rows:
	arq.write(row)
arq.close