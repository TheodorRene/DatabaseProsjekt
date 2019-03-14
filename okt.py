from app import DB
class treningsokt:

    def __init__(self, treningsokt_id,dato = None, varighet = None,personlig_form = None, prestasjon = None, senter_id = None, pnr=None):

        if (dato == None):
            self.treningsokt_id = treningsokt_id
            self.dato, self.varighet, self.personlig_form, self.prestasjon, self.senter_id, self.pnr\
            =\
            DB.getCol_db("treningsokt",1,"dato","varighet","personlig_form","prestasjon","senter_id","pnr")
        else:
            self.treningsokt_id, self.dato, self.varighet = treningsokt_id, dato, varighet
            self.personlig_form, self.prestasjon, self.senter_id  = prestasjon, senter_id, personlig_form

    def save


if __name__ == "__main__":
    test = treningsokt(1)
    print(test.dato)
    print(test.varighet)

