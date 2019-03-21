from database import DB

class Ovelse_i_ovelsegruppe:

    def __init__(self, ovelse_id, ovelsegruppe_id):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.ovelse_id = ovelse_id
        self.ovelsegruppe_id = ovelsegruppe_id


    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_ovelsegruppe_relasjon VALUES ({self.ovelse_id},'{self.ovelsegruppe_id}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
