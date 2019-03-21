from database import DB


class Treningssenter:
    def __init__(self, id_senter, navn=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.navn = navn if navn else self.get_senter_db(id_senter, "navn")

    def get_senter_db(self, id_senter, col):
        '''
        Gets an entry in the database with id_senter. Projects only the given column, given by col.
        :param id_senter:
        :param col: The column to be projected
        :return: Returns single entry
        '''
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