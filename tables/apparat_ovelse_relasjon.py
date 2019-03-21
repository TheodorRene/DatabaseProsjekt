from database import DB

class ApparatOvelseRelasjon:
    def __init__(self, apparat_id, ovelse_id):
        self.apparat_id = apparat_id
        self.ovelse_id = ovelse_id

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO apparat_ovelse_relasjon VALUES ({self.apparat_id},'{self.ovelse_id}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
