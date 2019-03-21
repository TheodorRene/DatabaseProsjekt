from database import DB


class Apparat:
    # legger til apparat i databasen hvis du gir apparat_id, navn og beskrivelse,
    # henter fra db hvis du kun gir apparat_id

    def __init__(self, apparat_id, navn=None, beskrivelse=None):
        self.apparat_id = apparat_id
        self.navn = navn if navn else self.get_person_db("navn")
        self.beskrivelse = beskrivelse if beskrivelse else self.get_person_db("beskrivelse")

    def get_person_db(self, col):
        con = DB.get_connection()
        db_req= f"SELECT {col} FROM apparat WHERE apparat_id={self.apparat_id}"
        result = con.execute(db_req).fetchone()[0]
        return result

    # Vil egentlig legge inn en test for å sjekke om navn og pnr er annerledes enn
    # hva db sier før det gjøres oppdateringer
    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO apparat (apparat_id,navn,beskrivelse) VALUES ({self.apparat_id},'{self.navn}','{self.beskrivelse}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
