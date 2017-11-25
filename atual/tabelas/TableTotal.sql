CREATE TABLE total
(
id SERIAL,
cod_ponto int,
bruto float[],
tratado float[],
CONSTRAINT key_total PRIMARY KEY (id),
CONSTRAINT localizacao FOREIGN KEY (cod_ponto) REFERENCES ponto
);