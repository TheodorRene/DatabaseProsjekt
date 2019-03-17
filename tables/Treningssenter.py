from database import DB


class Treningssenter:
    def __init__(self, id_senter, navn=None):
        self.id_senter = id_senter
        self.navn = navn if navn else self.get_column_db(id_senter, "navn")


    # return column
    def get_column_db(self, id_senter, col):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {col} FROM person WHERE treningssenter_id={id_senter}"
        result = cursor.execute(db_req).fetchone()[0]
        return result

    def save(self):
        con = DB.getConnection()
        cursor = con.cursor()
        db_req = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.id_senter});"
        cursor.execute(db_req)
        con.commit()
        con.close()