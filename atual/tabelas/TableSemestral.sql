CREATE TABLE semestral
(
id SERIAL,
cod_ponto int,
bruto float[],
tratado float[],
data_anual date,
CONSTRAINT key_semestral PRIMARY KEY (id),
CONSTRAINT localizacao FOREIGN KEY (cod_ponto) REFERENCES ponto
);