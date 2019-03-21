from database import DB


''''
create table ovelse_pa_apparat(
    ovelse_id INTEGER NOT NULL,
    antall_kilo INTEGER,
    antall_set INTEGER,
    apparat_id INTEGER NOT NULL,
    PRIMARY KEY(ovelse_id),
    FOREIGN KEY (apparat_id) REFERENCES apparat(apparat_id)
        ON DELETE CASCADE ON UPDATE CASCADE
    FOREIGN KEY(ovelse_id) REFERENCES ovelse(ovelse_id)
);
'''

class Ovelse_pa_apparat:
    # legger til ovelse_pa_apparat i databasen hvis du gir alle attributer,
    # henter fra db hvis du kun gir pk

    def __init__(self, ovelse_id, antall_kilo=None, antall_set=None, apparat_id=None):
        self.ovelse_id = int(ovelse_id)
        self.antall_kilo = int(antall_kilo if antall_kilo else self.get_person_db("antall_kilo"))
        self.antall_set = int(antall_set if antall_set else self.get_person_db("antall_set"))
        self.apparat_id = int(apparat_id if apparat_id else self.get_person_db("apparat_id"))

    def get_person_db(self, col):
        con = DB.get_connection()
        db_req= f"SELECT {col} FROM ovelse_pa_apparat WHERE ovelse_id={self.ovelse_id}"
        result = con.execute(db_req).fetchone()[0]
        return result

    # Vil egentlig legge inn en test for å sjekke om navn og pnr er annerledes enn
    # hva db sier før det gjøres oppdateringer
    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_pa_apparat VALUES ({self.ovelse_id}, {self.antall_kilo},{self.antall_set},{self.apparat_id});"
        cursor.execute(db_req)
        con.commit()
        con.close()
