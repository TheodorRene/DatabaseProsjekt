from database import DB


class Person:
    # legger til person i databasen hvis du gir navn og pnr, henter fra db hvis du kun gir pnr
    def __init__(self, pnr, navn=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.pnr = pnr
        self.navn = navn if navn else self.get_person_db("navn")


    def get_person_db(self, col):
        '''
        Gets an entry in the database with self.{id_field}. Projects only the given column, given by col.
        :param col: The column to be projected
        :return: Returns single entry
        '''
        con = DB.getConnection()
        db_req= f"SELECT {col} FROM person WHERE pnr={self.pnr}"
        result = con.execute(db_req).fetchone()[0]
        return result


    def save(self):
        con = DB.getConnection()
        cursor = con.cursor()
        db_req = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.pnr});"
        cursor.execute(db_req)
        con.commit()
        con.close()
