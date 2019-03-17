from abc import ABC, abstractmethod
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

    # Retrieve N treningsokter from DB. only PK here
    @abstractmethod
    def get_n_okter(n):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT treningsokt_id FROM treningsokt ORDER BY dato LIMIT {n};"
        result = [el[0] for el in cursor.execute(db_req).fetchall()]
        con.close()
        return result

if __name__=="__main__":
    test = Treningssenter(143, "3t")
    test.save()
    print(test.navn)

