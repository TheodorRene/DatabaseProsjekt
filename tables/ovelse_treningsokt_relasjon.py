from database import DB

class OvelseTreningsoktRelasjon:
    # legger til forbindelse mellom ovelse og treningsokt, henter fra db hvis du kun gir gruppeovelse_id
    def __init__(self, ovelse_id, treningsokt_id):
        self.ovelse_id = ovelse_id
        self.treningsokt_id = treningsokt_id

    """def get_gruppeovelse_db(self, col):
        con = DB.get_connection()
        db_req = f"SELECT {col} FROM ovelsegruppe WHERE ovelsegruppe_id={self.ovelsegruppe_id}"
        result = con.execute(db_req).fetchone()[0]
        return result"""

    # lagrer objektendringene i databasen
    def save(self):
        con = DB.get_connection()
        #con.execute("PRAGMA foreign_keys = ON") #Enable foreign keys
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_treningsokt_relasjon VALUES ({self.ovelse_id},'{self.treningsokt_id}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
