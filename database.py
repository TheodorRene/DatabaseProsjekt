from abc import ABC, abstractmethod
from tables import *
import sqlite3
TRENINGDB = "trening.db"


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

    # Retrieve N treningsokter from DB. 
    @abstractmethod
    def get_n_okter(n):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT dato,varighet,personlig_form,prestasjon,navn FROM treningsokt NATURAL JOIN treningssenter ORDER BY dato DESC LIMIT {n} ;"
        result = cursor.execute(db_req).fetchall()
        con.close()
        return result

    @abstractmethod
    # returnerer objektet med gitt pk dersom det finnes, returnerer None ellers
    def instance_exists(instance):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT * FROM {instance} WHERE {instance.pk_field}={instance.pk}"
        result = cursor.execute(db_req).fetchone()
        return result


if __name__=="__main__":
    treningssenter = Treningssenter(10, navn="Yoboi")
    print(treningssenter.navn)
    print(DB.instance_exists(treningssenter))

