import sqlite3
# Cream una connexió per a la BD (la BD es crearà al directori BD)
con = sqlite3.connect("./BD/tutorialalumnes.db")
cur = con.cursor()
# A continuació cream la taula amb l'estructura desitjada
con.execute("CREATE TABLE LlistatAlumnes (IdAlumne INTEGER NOT NULL PRIMARY KEY ASC, Llinatge1 TEXT, Llinatge2 TEXT, Nom TEXT)")
instruccions= """
INSERT INTO "LlistatAlumnes" VALUES(1,'ALLO','FLAQUER','JULIA');
INSERT INTO "LlistatAlumnes" VALUES(2,'CHEN','QIU','JUN YI');
INSERT INTO "LlistatAlumnes" VALUES(3,'CHMIEL','ARAYA','FERNANDO ALFONSO');
INSERT INTO "LlistatAlumnes" VALUES(4,'FERNÁNDEZ','MESQUIDA','IVÁN');
INSERT INTO "LlistatAlumnes" VALUES(5,'FERNÁNDEZ','URRETA','IGNACIO JAEL');
INSERT INTO "LlistatAlumnes" VALUES(6,'JIMÉNEZ','FERNÁNDEZ','JORDI');
INSERT INTO "LlistatAlumnes" VALUES(7,'LEBRERO','RODENAS','NEREA');
INSERT INTO "LlistatAlumnes" VALUES(8,'LLABRÉS','IGLESIAS','JESÚS');
INSERT INTO "LlistatAlumnes" VALUES(9,'LOMA','FULLANA','JAVIER');
INSERT INTO "LlistatAlumnes" VALUES(10,'MARTÍN DE LA FUENTE','MATEU','MARCOS');
INSERT INTO "LlistatAlumnes" VALUES(11,'MARTINO','ROMERO','JORDI');
INSERT INTO "LlistatAlumnes" VALUES(12,'NAVÍO','FRAU','ALBERT');
INSERT INTO "LlistatAlumnes" VALUES(13,'OBRADOR','PONS','JULIÀ');
INSERT INTO "LlistatAlumnes" VALUES(14,'PIMENTEL','LORENTE','VÍCTOR');
INSERT INTO "LlistatAlumnes" VALUES(15,'PIÑA','SUAREZ','OSCAR');
INSERT INTO "LlistatAlumnes" VALUES(16,'QUIROGA','GUTIÉRREZ','DIEGO ALEJANDRO');
INSERT INTO "LlistatAlumnes" VALUES(17,'RAMÍREZ','ARCOS','ALEJANDRO');
INSERT INTO "LlistatAlumnes" VALUES(18,'RAMOS','CHACÓN','LUCÍA');
INSERT INTO "LlistatAlumnes" VALUES(19,'ROSSELLÓ','BARAHONA','MARIONA');
INSERT INTO "LlistatAlumnes" VALUES(20,'SANS','CUENCA','DAVID');
INSERT INTO "LlistatAlumnes" VALUES(21,'TUGORES','VIANA','VÍCTOR');
"""
# Ara executarem totes les instruccions que hem ficat a instruccions
cur.executescript(instruccions)
# Confirmam tots els canvis
con.commit()
# Tancam la connexió de BD
con.close()