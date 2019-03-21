INSERT INTO treningssenter VALUES (1,"SIT gløshaugen");
INSERT INTO treningssenter VALUES (2,"SIT dragvoll");
INSERT INTO treningssenter VALUES (3,"SIT solsiden");
INSERT INTO treningssenter VALUES (4,"SIT Moholt");

INSERT INTO person VALUES (1,"Theodor René Carlsen");
INSERT INTO person VALUES (2,"Eivind Kopperud");
INSERT INTO person VALUES (3,"Andreas");

INSERT INTO ovelse_uten_apparat VALUES (1,"Du dytter jorda nedover");
INSERT INTO ovelse_uten_apparat VALUES (2,"Du dytter luft nedover");
INSERT INTO ovelse_uten_apparat VALUES (3,"Du spinner");

INSERT INTO ovelse_uten_apparat VALUES (7,"Du gjør 2010-trenden 'planking' - bare du trener!");

INSERT INTO apparat VALUES(1, "Benk", "Benk som kan flyttes og justere vinkel");
INSERT INTO apparat VALUES(2, "Skråbenk-stativ", "Fastmontert forbeholdt skråbenkpress");
INSERT INTO apparat VALUES(3, "Pull up-stang", "Fastmontert vertikal stang");
INSERT INTO apparat VALUES(4, "Lat pulldown-stativ", "Fastmontert lat pulldown-stativ med karabinkrok");


INSERT INTO apparat_ovelse_relasjon VALUES(2,6);
INSERT INTO apparat_ovelse_relasjon VALUES(4,4);
INSERT INTO apparat_ovelse_relasjon VALUES(4,5);
INSERT INTO apparat_ovelse_relasjon VALUES(4,8);
INSERT INTO apparat_ovelse_relasjon VALUES(4,9);


INSERT INTO ovelse_pa_apparat VALUES (4, 50, 4);
INSERT INTO ovelse_pa_apparat VALUES (5, 40, 5);
INSERT INTO ovelse_pa_apparat VALUES (6, 20, 10);
INSERT INTO ovelse_pa_apparat VALUES (8, 40, 5);
INSERT INTO ovelse_pa_apparat VALUES (9, 50, 4);
INSERT INTO ovelse_pa_apparat VALUES (10, 5, 5);
INSERT INTO ovelse_pa_apparat VALUES (11, 5, 5);


INSERT INTO ovelse VALUES (1,"Pushups");
INSERT INTO ovelse VALUES (2,"Situps");
INSERT INTO ovelse VALUES (3,"Backflip");
INSERT INTO ovelse VALUES (4,"Lat pull close 50/4");
INSERT INTO ovelse VALUES (5,"Lat pull close 40/5");
INSERT INTO ovelse VALUES (6,"Skråbenk 20/5");
INSERT INTO ovelse VALUES (7,"Planken");
INSERT INTO ovelse VALUES (8,"Lat pull wide 40/5");
INSERT INTO ovelse VALUES (9,"Lat pull wide 50/4");
INSERT INTO ovelse VALUES (10,"Pull up 5/5");
INSERT INTO ovelse VALUES (11,"Chin up 5/5");


INSERT INTO ovelsegruppe VALUES (1,"Ryggøvelser");
INSERT INTO ovelsegruppe VALUES (2,"Bryst");
INSERT INTO ovelsegruppe VALUES (3,"Triceps");
INSERT INTO ovelsegruppe VALUES (4,"Koordinasjon");


INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (1, 2);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (1, 3);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (3, 4);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (4, 1);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (5, 1);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (6, 2);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (7, 2);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (8, 1);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (9, 1);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (10, 1);
INSERT INTO ovelse_ovelsegruppe_relasjon VALUES (11, 1);

INSERT INTO treningsokt VALUES (1, "1997-22-04",50, 5, 5, 3,1);
INSERT INTO treningsokt VALUES (2, "1998-20-05",55, 3, 6, 1,2);

INSERT INTO ovelse_treningsokt_relasjon VALUES (1, 1);
INSERT INTO ovelse_treningsokt_relasjon VALUES (1, 2);
INSERT INTO ovelse_treningsokt_relasjon VALUES (1, 3);
INSERT INTO ovelse_treningsokt_relasjon VALUES (1, 4);
INSERT INTO ovelse_treningsokt_relasjon VALUES (2, 5);
INSERT INTO ovelse_treningsokt_relasjon VALUES (2, 6);
INSERT INTO ovelse_treningsokt_relasjon VALUES (2, 7);
INSERT INTO ovelse_treningsokt_relasjon VALUES (2, 8);
