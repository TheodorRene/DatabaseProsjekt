from database import DB

'''
create table ovelse(
    ovelse_id INTEGER NOT NULL,
    navn varchar(255),
    PRIMARY KEY(ovelse_id)
);
'''

class Ovelse:
    # legger til ovelse i databasen hvis du gir navn og ovelse_id, henter fra db hvis du kun gir ovelse_id
    def __init__(self, ovelse_id, navn=None):
        self.ovelse_id = ovelse_id
        self.navn = navn if navn else self.get_ovelse_db("navn")

    def get_ovelse_db(self, col):
        con = DB.get_connection()
        db_req = f"SELECT {col} FROM ovelse WHERE ovelse_id={self.ovelse_id}"
        result = con.execute(db_req).fetchone()[0]
        return result

    # lagrer objektendringene i databasen
    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse VALUES ({self.ovelse_id},'{self.navn}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
