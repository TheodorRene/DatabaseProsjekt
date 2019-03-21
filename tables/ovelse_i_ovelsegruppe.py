from database import DB

class Ovelse_i_ovelsegruppe:
    # legger til forbindelse mellom gruppeovelse og ovelse, henter fra db hvis du kun gir gruppeovelse_id
    def __init__(self, ovelse_id, ovelsegruppe_id):
        self.ovelse_id = ovelse_id
        self.ovelsegruppe_id = ovelsegruppe_id

    """def get_gruppeovelse_db(self, col):
        con = DB.get_connection()
        db_req = f"SELECT {col} FROM ovelsegruppe WHERE ovelsegruppe_id={self.ovelsegruppe_id}"
        result = con.execute(db_req).fetchone()[0]
        return result"""

    # lagrer objektendringene i databasen
    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_i_ovelsegruppe VALUES ({self.ovelse_id},'{self.ovelsegruppe_id}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
