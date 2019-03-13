from abc import ABC, abstractmethod
import sqlite3

TRENINGDB = "trening3.db"

class Person:
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

    def save(self):
        con1 = DB.getConnection()
        con = con1.cursor()
#        dbReq = f"SELECT navn,pnr FROM person WHERE pnr={self.pn}"
#        navn,pnr = con.execute(dbReq).fetchone()
        dbReq = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.pnr});"
        con.execute(dbReq)
        con1.commit()
        con1.close()

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










