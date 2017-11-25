CREATE TABLE anual
(
id SERIAL,
cod_ponto int,
bruto float[],
tratado float[],
data_anual date,
CONSTRAINT key_anual PRIMARY KEY (id),
CONSTRAINT localizacao FOREIGN KEY (cod_ponto) REFERENCES ponto
);