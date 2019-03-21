DROP TABLE treningssenter;
DROP TABLE person;
DROP TABLE ovelse_uten_apparat;
DROP TABLE ovelsegruppe;
DROP TABLE ovelse;
DROP TABLE apparat;
DROP TABLE ovelse_treningsokt;
DROP TABLE ovelse_pa_apparat;
DROP TABLE ovelse_i_ovelsegruppe;
DROP TABLE treningsokt;
DROP TABLE apparat_ovelse_relasjon;

create table treningssenter(
    treningssenter_id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(treningssenter_id)
);

create table person(
    pnr INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(pnr)
);

create table ovelse_uten_apparat(
    ovelse_id INTEGER NOT NULL,
    beskrivelse varchar(255),
    PRIMARY KEY(ovelse_id),
    FOREIGN KEY (ovelse_id) REFERENCES ovelse(ovelse_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table ovelsegruppe(
    ovelsegruppe_id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(ovelsegruppe_id)
);

create table ovelse(
    ovelse_id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(ovelse_id)
);

create table apparat(
    apparat_id INTEGER NOT NULL,
    navn varchar(255),
    beskrivelse varchar(255),
    PRIMARY KEY(apparat_id)
);

create table ovelse_treningsokt_relasjon(
    ovelse_id  INTEGER NOT NULL,
    treningsokt_id INTEGER NOT NULL,
    PRIMARY KEY(treningsokt_id,ovelse_id)
    FOREIGN KEY (treningsokt_id) REFERENCES treningsokt(treningsokt_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ovelse_id) REFERENCES ovelse(ovelse_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table ovelse_pa_apparat(
    ovelse_id INTEGER NOT NULL,
    antall_kilo INTEGER,
    antall_set INTEGER,
    PRIMARY KEY(ovelse_id),
    FOREIGN KEY(ovelse_id) REFERENCES ovelse(ovelse_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table apparat_ovelse_relasjon(
    ovelse_id INTEGER NOT NULL,
    apparat_id INTEGER NOT NULL,
    apparat_id INTEGER NOT NULL,
    ovelse_id INTEGER NOT NULL,

    PRIMARY KEY(ovelse_id, apparat_id)
    FOREIGN KEY (ovelse_id) REFERENCES ovelse_pa_apparat(ovelse_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (apparat_id) REFERENCES apparat(apparat_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

create table ovelse_ovelsegruppe_relasjon(
    ovelse_id INTEGER NOT NULL,
    ovelsegruppe_id INTEGER NOT NULL,
    PRIMARY KEY(ovelse_id,ovelsegruppe_id),
    FOREIGN KEY (ovelsegruppe_id) REFERENCES ovelsegruppe(ovelsegruppe_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ovelse_id) REFERENCES ovelse(ovelse_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE treningsokt(
    treningsokt_id INTEGER NOT NULL,
    dato DATE, 
    varighet INTEGER,
    personlig_form INTEGER check (personlig_form between 0 and 10),
    prestasjon INTEGER check (prestasjon between 0 and 10),
    senter_id INTEGER NOT NULL,
    pnr INTEGER NOT NULL,
    PRIMARY KEY (treningsokt_id),
    FOREIGN KEY (senter_id) REFERENCES treningssenter(treningssenter_id)
        ON UPDATE CASCADE,
    FOREIGN KEY (pnr) REFERENCES person(pnr)
        ON DELETE CASCADE ON UPDATE CASCADE
    );



