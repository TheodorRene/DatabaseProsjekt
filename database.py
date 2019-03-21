from abc import ABC, abstractmethod
import sqlite3
TRENINGDB = "trening.db"


# generell DB klasse, kan sikkert brukes til veldig generelle kall
# nå blir det nesten som at klassene i python speilier tabeller i db, litt usikker på hva som er ideelt
class DB(ABC):
    '''
    A general database class that is used for (almost) all SQL queries.
    '''

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
        '''
        General project function that returns a given record in a table with pk=pk, with the fields defined in args.
        :param pk: The record's primary key value
        :param args: An arbritrary number of fields, that will be projected.
        :return: A record with the given fields.
        '''
        con = DB.get_connection()
        cursor = con.cursor()

        # Make a string for the fields, used in the database request.
        fields = ""
        for num,el in enumerate(args):
            if (num != (len(args)-1)):
                fields += " " + el + ","
            else:
                fields += el

        db_req = f"SELECT {arguments} FROM {table} WHERE {table}_id={pk};"
        result = cursor.execute(db_req).fetchone()
        con.close()
        return result

    @abstractmethod
    def get_n_okter(n):
        '''
        Get information about the n previous treningsokts
        :param n: Number of treningsokt wanted
        :return: Returns the query result for the n last treningsokts
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT dato,varighet,personlig_form,prestasjon,navn FROM treningsokt NATURAL JOIN treningssenter ORDER BY dato DESC LIMIT {n} ;"
        result = cursor.execute(db_req).fetchall()
        con.close()
        return result

    @abstractmethod
    def get_personal_record(ovelse):
        '''
        Gives the personal best for a ovelse
        :param ovelse: A ovelse which the user wants to get the personal best
        :return: Returns the query result for the personal best
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        if DB.has_apparat(ovelse):
            db_req= f"SELECT ovelse_id,MAX(antall_kilo*antall_set) FROM ovelse_pa_apparat NATURAL JOIN ovelse WHERE navn LIKE '{ovelse}%';"
            pk = cursor.execute(db_req).fetchall()[0][0]
            db_req_2 = f"SELECT * FROM ovelse_pa_apparat NATURAL JOIN ovelse WHERE ovelse_id={int(pk)};"
            result = cursor.execute(db_req_2).fetchone()

        else:
            db_req= f"SELECT * FROM ovelse_uten_apparat NATURAL JOIN ovelse WHERE navn LIKE '{ovelse}%';"
            result = cursor.execute(db_req).fetchall()
        con.close()
        return result

    @abstractmethod
    def has_apparat(ovelse):
        '''
        Tells whether the ovelse has a apparat or not.
        :param ovelse: The ovelse wanted to inspect
        :return: Returns a bool value
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        query_pa_apparat = f"SELECT * FROM ovelse_pa_apparat NATURAL JOIN ovelse WHERE navn LIKE '{ovelse}%'"
        has_apparat = cursor.execute(query_pa_apparat).fetchall()
        con.close()
        return bool(has_apparat)

    @abstractmethod
    def ovelse_log_in_interval(ovelse_id, start, end):
        '''
        See all entries with a given ovelse, that happened between 'start' and 'end'
        :param ovelse_id: ID of the specified ovelse
        :param start: Start of time interval
        :param end: End of time interval
        :returns: Returns the query result, and a bool indicating whether if the ovelse has an apparat or not
        '''
        format_start = f"Datetime('{start}')"
        format_end = f"Datetime('{end}')"
        con = DB.get_connection()
        cursor = con.cursor()

        # SQL queries that connects the different ovelses with treningsokt
        table_pa_apparat = "ovelse_pa_apparat NATURAL JOIN ovelse NATURAL JOIN ovelse_treningsokt_relasjon NATURAL JOIN treningsokt"
        table_uten_apparat = "ovelse_uten_apparat NATURAL JOIN ovelse NATURAL JOIN ovelse_treningsokt_relasjon NATURAL JOIN treningsokt"

        # Fields wanted from the query
        fields_pa_apparat = "dato, navn, antall_kilo, antall_set"
        fields_uten_apparat = "dato, navn, beskrivelse"

        # Constraint that make sure the ovelse is in a specified interval
        constraint = f"(ovelse_id={ovelse_id} AND dato >= {format_start} AND dato <= {format_end})"

        query_pa_apparat = f"SELECT {fields_pa_apparat} FROM {table_pa_apparat} WHERE {constraint}"
        ovelse_pa_apparat = cursor.execute(query_pa_apparat).fetchall()
        if ovelse_pa_apparat:
            return ovelse_pa_apparat, True

        query_uten_apparat = f"SELECT {fields_uten_apparat} FROM {table_uten_apparat} WHERE {constraint}"
        ovelse_uten_apparat = cursor.execute(query_uten_apparat).fetchall()
        con.close()
        return ovelse_uten_apparat, False


    @abstractmethod
    def get_ovelser_in_ovelsegruppe(gruppe_id):
        '''
        :return: The queryset of all the ovelser in the given ovelsegruppe.
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT ovelse_id FROM ovelse_ovelsegruppe_relasjon NATURAL JOIN ovelsegruppe WHERE ovelsegruppe_id={gruppe_id};"
        result = [el[0] for el in cursor.execute(db_req).fetchall()]
        liste = []
        print("Ovelser fra øvelssesgrupe:\n" + str(result))
        for el in result:
            db_req_2= f"SELECT navn FROM ovelse WHERE ovelse_id={el};"
            liste.append(cursor.execute(db_req_2).fetchone()[0])
        con.close()
        return liste

    @abstractmethod
    def project_table(table, project_cols):
        '''
        :param table: The table which the information should be taken from
        :param project_cols: A string identifying which columns that should be projected from the query
        :return: A queryset with the given columns
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {project_cols} FROM {table};"

        if "," in project_cols:
            result = cursor.execute(db_req).fetchall()

        else:
            result = [el[0] for el in cursor.execute(db_req).fetchall()]

        con.close()
        return result

    @abstractmethod
    def project_table_where(project, table, lookup, identifier):
        '''
        :param project: Column you want to project
        :param table: Table you want to look up
        :param identifier: The unique ID/name you have
        :return: Returns the projected entity
        '''
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"SELECT {project} FROM {table} WHERE {lookup} = '{identifier}';"
        result = cursor.execute(db_req).fetchone()
        con.close()
        return result[0]
