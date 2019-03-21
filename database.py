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
    def get_name_from_table(name,table):
        # get db
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {name} FROM {table};"
        result = cursor.execute(db_req).fetchall()
        return [el[0] for el in result]
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
    def getPersonalRecordApparat(ovelse):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req= f"SELECT ovelse_id,MAX(antall_kilo*antall_set) FROM ovelse_pa_apparat NATURAL JOIN ovelse WHERE navn LIKE '{ovelse}%';"
        result = cursor.execute(db_req).fetchall()
        con.close()
        return result

    @abstractmethod
    def getPersonalRecord(ovelse):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req= f"SELECT * FROM ovelse_uten_apparat NATURAL JOIN ovelse WHERE navn LIKE '{ovelse}%';"
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

    @abstractmethod
    def get_ovelsegrupper():
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT navn,ovelsegruppe_id FROM ovelsegruppe"  # WHERE {gruppe_id}={1}
        result = cursor.execute(db_req).fetchall()
        con.close()
        return result

    @abstractmethod
    def get_id_of_ovelsegruppe(navn):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT ovelsegruppe_id FROM ovelsegruppe WHERE navn='{navn}'; "  # WHERE {gruppe_id}={1}
        print(navn)
        result = cursor.execute(db_req).fetchone()[0]
        con.close()
        return result

    @abstractmethod
    def get_ovelser_in_ovelsegruppe(gruppe_id):
        con = DB.get_connection()
        cursor = con.cursor()
        print(gruppe_id)
        db_req = f"SELECT ovelse_id FROM ovelse_ovelsegruppe_relasjon NATURAL JOIN ovelsegruppe WHERE ovelsegruppe_id={gruppe_id};"
        result = [el[0] for el in cursor.execute(db_req).fetchall()]
        liste = []
        print("Ovelser fra øvelssesgrupe:\n" + str(result))
        for el in result:
            db_req_2= f"SELECT navn FROM ovelse WHERE ovelse_id={el};"
            liste.append(cursor.execute(db_req_2).fetchone()[0])
        con.close()
        return liste


if __name__=="__main__":
    #treningssenter = Treningssenter(10, navn="Yoboi")
    #print(treningssenter.navn)
    #print(DB.instance_exists(treningssenter))
    pass


