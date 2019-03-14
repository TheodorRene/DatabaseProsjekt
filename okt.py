from app import DB
class treningsokt:

    def __init__(self, treningsokt_id,dato = None, varighet = None,personlig_form = None, prestasjon = None, senter_id = None, pnr=None):

        if (dato == None):
            self.treningsokt_id = treningsokt_id
            self.dato, self.varighet, self.personlig_form, self.prestasjon, self.senter_id, self.pnr\
            =\
            DB.getCol_db("treningsokt",treningsokt_id,"dato","varighet","personlig_form","prestasjon","senter_id","pnr")
        else:
            self.treningsokt_id, self.dato, self.varighet = treningsokt_id, dato, varighet
            self.personlig_form, self.prestasjon, self.senter_id, self.pnr  = prestasjon, senter_id, personlig_form, pnr


    def save(self):
        con = DB.getConnection()
        c = con.cursor()

        dbReq = f"INSERT INTO treningsokt VALUES (" +\
        f"{self.treningsokt_id}, '{self.dato}', '{self.varighet}', '{self.personlig_form}', '{self.prestasjon}','{self.senter_id}','{self.pnr}')"

        c.execute(dbReq)
        con.commit()
        con.close()


if __name__ == "__main__":
    print(DB.getNOkter(2))
    #eksempel på å legge til i database
    #test = treningsokt(5,"1232",33,"bra",3,2,1)
    #test.save()

    #Eksempel på å hente fra database
    #test = treningsokt(5)

