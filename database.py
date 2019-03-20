from abc import ABC, abstractmethod
from tables import *
import sqlite3
TRENINGDB = "trening.db"


# generell DB klasse, kan sikkert brukes til veldig generelle kall
# nå blir det nesten som at klassene i python speilier tabeller i db, litt usikker på hva som er ideelt
class DB(ABC):

    @abstractmethod
    def get_connection():
        '''
        Makes a connection to a database
        :return: Returns a connection variable to the database
        '''
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
        '''
        Get information about the n previous treningsokts
        :param n: Number of treningsokt wanted
        :return: Returns the query result
        '''
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

    @abstractmethod
    def ovelse_log_in_interval(ovelse_id, start, end):
        '''
        See all entries with a given ovelse, that happened between 'start' and 'end'
        :param ovelse_id: ID of the specified ovelse
        :param start: Start of time interval
        :param end: End of time interval
        :return: Returns the query result
        '''
        format_start = f"Datetime('{start}')"
        format_end = f"Datetime('{end}')"
        con = DB.get_connection()
        cursor = con.cursor()

        # SQL query that connects ovelse_pa_apparat with treningsokt
        table_pa_apparat = "ovelse_pa_apparat NATURAL JOIN ovelse NATURAL JOIN ovelse_treningsokt_relasjon NATURAL JOIN treningsokt"

        # Constraint that make sure the ovelse is in a specified interval
        constraint = f"(ovelse_id={ovelse_id} AND dato >= {format_start} AND dato <= {format_end})"

        query_pa_apparat = f"SELECT * FROM {table_pa_apparat} WHERE {constraint}"
        ovelse_pa_apparat = cursor.execute(query_pa_apparat).fetchall()
        if ovelse_pa_apparat:
            return ovelse_pa_apparat

        # SQL query that connects ovelse_uten_apparat with treningsokt
        table_uten_apparat = "ovelse_uten_apparat NATURAL JOIN ovelse NATURAL JOIN ovelse_treningsokt_relasjon NATURAL JOIN treningsokt"

        query_uten_apparat = f"SELECT * FROM {table_uten_apparat} WHERE {constraint}"
        ovelse_uten_apparat = cursor.execute(query_uten_apparat).fetchall()
        return ovelse_uten_apparat


if __name__=="__main__":
    print(DB.ovelse_log_in_interval(1, '1900-05-06', '2208-05-08'))

