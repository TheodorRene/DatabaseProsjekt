from database import DB


class Person:
    # legger til person i databasen hvis du gir navn og pnr, henter fra db hvis du kun gir pnr
    def __init__(self, pnr, navn=None):
        self.pnr = pnr
        self.navn = navn if navn else self.get_person_db("navn")

    def get_person_db(self, col):
        con = DB.getConnection()
        db_req= f"SELECT {col} FROM person WHERE pnr={self.pnr}"
        result = con.execute(db_req).fetchone()[0]
        return result

    # Vil egentlig legge inn en test for å sjekke om navn og pnr er annerledes enn
    # hva db sier før det gjøres oppdateringer
    def save(self):
        con = DB.getConnection()
        cursor = con.cursor()
        db_req = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.pnr});"
        cursor.execute(db_req)
        con.commit()
        con.close()
