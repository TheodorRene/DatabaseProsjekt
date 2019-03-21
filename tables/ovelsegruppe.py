from database import DB

class Ovelsegruppe:
    # legger til gruppeovelse i databasen hvis du gir navn og gruppeovelse_id, henter fra db hvis du kun gir gruppeovelse_id
    def __init__(self, ovelsegruppe_id, navn=None):
        self.ovelsegruppe_id = ovelsegruppe_id
        self.navn = navn if navn else self.get_ovelse_db("navn")

    def get_gruppeovelse_db(self, col):
        con = DB.get_connection()
        db_req = f"SELECT {col} FROM ovelsegruppe WHERE ovelsegruppe_id={self.ovelsegruppe_id}"
        result = con.execute(db_req).fetchone()[0]
        return result

    # lagrer objektendringene i databasen
    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelsegruppe VALUES ({self.ovelsegruppe_id},'{self.navn}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
