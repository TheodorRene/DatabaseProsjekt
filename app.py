from abc import ABC, abstractmethod
import sqlite3

TRENINGDB = "trening3.db"

class Person:
    #legger til person i databasen hvis du gir navn og pnr, henter fra db hvis du kun gir pnr
    def __init__(self, pnr, navn=None):
        if navn==None:
            self.navn = ""
            self.pnr = pnr
            self.navn = self.getPerson_db(pnr,"navn")
        else:
            self.navn = navn
            self.pnr = pnr

    def getPerson_db(self,pnr,col):
        con = DB.getConnection()
        dbReq= f"select {col} from person where pnr={self.pnr}"
        result = con.execute(dbReq).fetchone()[0]
        return result

    #Vil egentlig legge inn en test for å sjekke om navn og pnr er annerledes enn
    #hva db sier før det gjøres oppdateringer
    def save(self):
        con1 = DB.getConnection()
        con = con1.cursor()
        dbReq = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.pnr});"
        con.execute(dbReq)
        con1.commit()
        con1.close()

#generell DB klasse, kan sikkert brukes til veldig generelle kall
#nå blir det nesten som at klassene i python speilier tabeller i db, litt usikker på hva som er ideelt
class DB(ABC):

    @abstractmethod
    def getConnection():
        try:
            global TRENINGDB
            conn = sqlite3.connect(TRENINGDB)
        except sqlite3.Error as er:
            raise Exception("Could not find database file")
        return conn

    @abstractmethod
    def getCol_db(table, pk, *args):
        #get db
        con = DB.getConnection()
        c = con.cursor()

        #lag comma seperated values from args
        arguments = ""
        for num,el in enumerate(args):
            if (num != (len(args)-1)):
                arguments += " " + el + ","
            else:
                arguments += el

        dbReq = f"SELECT {arguments} FROM {table} WHERE {table}_id={pk};"

        result = c.execute(dbReq).fetchone()
        c.close()
        return result

    def insertRow_db(table):
        dbReq = f"INSERT INTO {table} VALUES ({val});"



class Treningssenter:
    def __init__(self,id_senter,navn=None):
        if navn == None:
            self.id_senter = id_senter
            self.navn = self.getColumn_db(id_senter,"navn")
        else:
            self.navn = navn
            self.id_senter = id_senter

    #return colum
    def getColumn_db(self,id_senter,col):
        con = DB.getConnection()
        c = con.cursor()
        dbReq = f"SELECT {col} FROM person WHERE treningssenter_id={id_senter}"
        result = c.execute(dbReq).fetchone()[0]
        return result

    def save(self):
        con1 = DB.getConnection()
        con = con1.cursor()
        dbReq = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.id_senter});"
        con.execute(dbReq)
        con1.commit()
        con1.close()


if __name__=="__main__":
    test = Treningssenter(143,"3t")
    test.save()
    print(test.navn)

