from database import DB

class OvelseTreningsoktRelasjon:

    def __init__(self, ovelse_id, treningsokt_id):
        self.ovelse_id = ovelse_id
        self.treningsokt_id = treningsokt_id

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_treningsokt_relasjon VALUES ({self.ovelse_id},'{self.treningsokt_id}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
