create table treningssenter(
    id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(id)
);

create table person(
    pnr INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(pnr)
);

create table ovelse_uten_apparat(
    id INTEGER NOT NULL,
    navn varchar(255),
    beskrivelse varchar(255),
    PRIMARY KEY(id)
);

create table ovelsegruppe(
    id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(id)
);

create table ovelse(
    id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(id)
);

create table apparat(
    id INTEGER NOT NULL,
    navn varchar(255),
    beskrivelse varchar(255),
    PRIMARY KEY(id)
);

create table ovelse_treningsokt(
    treningsokt_id INTEGER NOT NULL,
    ovelses_id  INTEGER NOT NULL,
    PRIMARY KEY(treningsokt_id,ovelses_id)
    FOREIGN KEY (treningsokt_id) REFERENCES treningsokt(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ovelses_id) REFERENCES ovelse(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table ovelse_pa_apparat(
    id INTEGER NOT NULL,
    antall_kilo INTEGER,
    antall_set INTEGER,
    apparat_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (apparat_id) REFERENCES apparat(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table ovelse_i_ovelsegruppe(
    ovelse_id INTEGER NOT NULL,
    ovelsegruppe_id INTEGER NOT NULL,
    PRIMARY KEY(ovelse_id,ovelsegruppe_id),
    FOREIGN KEY (ovelsegruppe_id) REFERENCES ovelsegruppe(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ovelse_id) REFERENCES ovelse(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE treningsokt(
    id INTEGER NOT NULL,
    dato DATE, 
    varighet INTEGER,
    personlig_form varchar(255),
    prestasjon INTEGER check (prestasjon between 0 and 10),
    senter_id INTEGER NOT NULL,
    pnr INTEGER NOT NULL,
    FOREIGN KEY (senter_id) REFERENCES treningssenter(id)
        ON UPDATE CASCADE,
    FOREIGN KEY (pnr) REFERENCES person(pnr)
        ON DELETE CASCADE ON UPDATE CASCADE
    );



