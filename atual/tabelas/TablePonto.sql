﻿CREATE TABLE ponto
(
id SERIAL,
lat NUMERIC,
lon NUMERIC,
CONSTRAINT PKey PRIMARY KEY (id)
);
INSERT INTO ponto (lat, lon) SELECT DISTINCT lat,lon FROM trmm ORDER BY lat;