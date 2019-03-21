from database import DB
class Treningsokt:

    def __init__(self, treningsokt_id,
                 dato=None, varighet=None,
                 personlig_form=None, prestasjon=None,
                 senter_id=None, pnr=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''

        if dato:
            self.treningsokt_id, self.dato, self.varighet = treningsokt_id, dato, int(varighet)
            self.personlig_form, self.prestasjon, self.senter_id, self.pnr  = int(prestasjon), int(senter_id), int(personlig_form), int(pnr)

        else:
            self.treningsokt_id = treningsokt_id
            self.dato, self.varighet, self.personlig_form, self.prestasjon, self.senter_id, self.pnr \
                = \
                DB.get_col_db("treningsokt", treningsokt_id, "dato", "varighet", "personlig_form", "prestasjon",
                        "senter_id", "pnr")

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO treningsokt VALUES (" +\
        f"{self.treningsokt_id}, '{self.dato}', {self.varighet}, {self.personlig_form}, {self.prestasjon}, {self.senter_id}, {self.pnr})"
        cursor.execute(db_req)
        con.commit()
        con.close()
