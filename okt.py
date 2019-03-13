class treningsokt:
    def __init__(self, treningsokt_id,dato = None, varighet = None,personlig_form = None, prestasjon = None, senter_id = None):
        if (dato = None):
            self.treningsokt_id = treningsokt_id
            getCol_db(treningsokt_id)

    def getCol_db(self,treningsok_id, *args):
        con = DB.getConnection()
        c = con.cursor()
        #lag comma seperated values from args
        dbReq = f"SELECT {args} FROM person WHERE treningssenter_id={id_senter}"
        result = c.execute(dbReq).fetchone()[0]
        return result

