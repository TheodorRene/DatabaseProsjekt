from abc import ABC, abstractmethod
import sqlite3
TRENINGDB = "trening3.db"


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

# generell DB klasse, kan sikkert brukes til veldig generelle kall
# nå blir det nesten som at klassene i python speilier tabeller i db, litt usikker på hva som er ideelt
class DB(ABC):

    @abstractmethod
    def get_connection():
        try:
            global TRENINGDB
            con = sqlite3.connect(TRENINGDB)
        except sqlite3.Error as er:
            raise Exception("Could not find database file")
        return con

    @abstractmethod
    def get_col_db(table, pk, *args):
        # get db
        con = DB.get_connection()
        cursor = con.cursor()

        # lag comma seperated values from args
        arguments = ""
        for num,el in enumerate(args):
            if (num != (len(args)-1)):
                arguments += " " + el + ","
            else:
                arguments += el

        db_req = f"SELECT {arguments} FROM {table} WHERE {table}_id={pk};"

        result = cursor.execute(db_req).fetchone()
        con.close()
        return result

    def insertRow_db(table):
        dbReq = f"INSERT INTO {table} VALUES ({val});"

    # Retrieve N treningsokter from DB. only PK here
    @abstractmethod
    def get_n_okter(n):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT treningsokt_id FROM treningsokt ORDER BY dato LIMIT {n};"
        result = [el[0] for el in cursor.execute(db_req).fetchall()]
        con.close()
        return result


class Treningssenter:
    def __init__(self, id_senter, navn=None):
        self.id_senter = id_senter
        self.navn = navn if navn else self.get_column_db(id_senter, "navn")


    # return column
    def get_column_db(self, id_senter, col):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {col} FROM person WHERE treningssenter_id={id_senter}"
        result = cursor.execute(db_req).fetchone()[0]
        return result

    def save(self):
        con = DB.getConnection()
        cursor = con.cursor()
        db_req = f"INSERT INTO person (navn,pnr) VALUES ('{self.navn}',{self.id_senter});"
        cursor.execute(db_req)
        con.commit()
        con.close()


if __name__=="__main__":
    test = Treningssenter(143, "3t")
    test.save()
    print(test.navn)

