from database import DB


class Treningssenter:
    def __init__(self, id_senter, navn=None):
        # METADATA
        self.pk_field = "treningssenter_id"

        # OBJEKTDATA
        self.pk = id_senter
        self.navn = navn if navn else self.get_column_db(id_senter, "navn")

    def __str__(self):
        #
        return "treningssenter"


    # return column
    def get_column_db(self, id_senter, col):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {col} FROM treningssenter WHERE treningssenter_id={id_senter}"
        result = cursor.execute(db_req).fetchone()[0]
        return result

    def save(self):
        con = DB.getConnection()
        cursor = con.cursor()
        db_req = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.id_senter});"
        cursor.execute(db_req)
        con.commit()
        con.close()