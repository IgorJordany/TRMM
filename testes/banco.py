import psycopg2
con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='')
cur = con.cursor()
sql = 'create table cidade (id serial primary key, nome varchar(100), uf varchar(2))'
