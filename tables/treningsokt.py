from database import DB
class Treningsokt:

    def __init__(self, treningsokt_id,
                 dato=None, varighet=None,
                 personlig_form=None, prestasjon=None,
                 senter_id=None, pnr=None):

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


if __name__ == "__main__":
    print(DB.get_n_okter(2))
    #eksempel på å legge til i database
    #test = treningsokt(5,"1232",33,"bra",3,2,1)
    #test.save()

    #Eksempel på å hente fra database
    #test = treningsokt(5)

