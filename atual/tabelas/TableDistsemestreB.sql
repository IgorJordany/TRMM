CREATE TABLE distsemestreB
(
id SERIAL,
codPonto int,
datPonto date,
codPonto1 int,
distBruta1 float[],
distTratada1 float[],
datPonto1 date,
codPonto2 int,
distBruta2 float[],
distTratada2 float[],
datPonto2 date,
codPonto3 int,
distBruta3 float[],
distTratada3 float[],
datPonto3 date,
codPonto4 int,
distBruta4 float[],
distTratada4 float[],
datPonto4 date,
codPonto5 int,
distBruta5 float[],
distTratada5 float[],
datPonto5 date,
codPonto6 int,
distBruta6 float[],
distTratada6 float[],
datPonto6 date,
CONSTRAINT keyDistSemestreb PRIMARY KEY (id),
CONSTRAINT estbponto FOREIGN KEY (codPonto) REFERENCES ponto,
CONSTRAINT estbponto1 FOREIGN KEY (codPonto1) REFERENCES ponto,
CONSTRAINT estbponto2 FOREIGN KEY (codPonto2) REFERENCES ponto,
CONSTRAINT estbponto3 FOREIGN KEY (codPonto3) REFERENCES ponto,
CONSTRAINT estbponto4 FOREIGN KEY (codPonto4) REFERENCES ponto,
CONSTRAINT estbponto5 FOREIGN KEY (codPonto5) REFERENCES ponto,
CONSTRAINT estbponto6 FOREIGN KEY (codPonto6) REFERENCES ponto
);
