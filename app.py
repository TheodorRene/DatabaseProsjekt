from abc import ABC, abstractmethod
import sqlite3

TRENINGDB = "trening3.db"

class Person:
    #legger til person i databasen hvis du gir navn og pnr, henter fra db hvis du kun gir pnr
    def __init__(self, pnr, navn=None):
        if navn==None:
            self.navn = ""
            self.pnr = pnr
            self.getPerson_db(pnr)
        else:
            self.navn = navn
            self.pnr = pnr

    def getPerson_db(self,pnr):
        con = DB.getConnection()
        dbReq= f"select navn from person where pnr={self.pnr}"
        navn = con.execute(dbReq).fetchone()[0]
        self.navn = navn

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

if __name__=="__main__":
    test = Person(143)
    print(test.navn)










