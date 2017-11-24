import logging
import os

import psycopg2
from psycopg2.extras import register_uuid
from psycopg2.extras import LoggingConnection

class BaseController():

    _connection = None
    _logger = None
    _tries = 0

    def __init__ (self):
        logging.basicConfig(level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)
        self._connection = self._init_connection()

    def __del__(self):
        if self._connection:
            self._connection.close()

    def get_connection(self):
        return self._connection

    def _init_connection(self):

        database_name = os.getenv('DATABASE','example')
        config = {
            'user': os.getenv('DB_USER',os.getenv('USER')),
            'database': database_name,
            'password': os.getenv('DB_PASSWORD',None),
            'host': os.getenv('DB_HOST','localhost'),
        }

        psycopg2.extensions.register_type(register_uuid())
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

        conn = None

        try:
            try:
                conn = psycopg2.connect(connection_factory=LoggingConnection, **config )
                conn.initialize(self._logger)
            except Exception as e:
                print("Database connection problem")
                self._logger.exception("Database connection problem")
                if os.getenv('CREATE_SCHEMA_IF_MISSING', "false") == "true":
                    #Unlikely to be the problem
                    config['database'] = 'postgres'
                    conn = psycopg2.connect(connection_factory=LoggingConnection, **config )
                    conn.initialize(self._logger)
                    cur = conn.cursor()
                    cur.execute('CREATE DATABASE ' + database_name)
                    conn.commit()
                    conn.close()
                    self._tries = self._tries + 1
                    if self._tries < 2:
                        return self._init_connection()
                    else:
                        return None
        except Exception as e:
            self._logger.exception("Database connection problem")

        self._create_database(conn, database_name)

        return conn

    def _create_database(self, conn, database_name):

        if os.getenv('CREATE_SCHEMA_IF_MISSING', "false") == "true":
            cur = conn.cursor()

            cur.execute("""SELECT table_name, table_schema FROM information_schema.tables
                                  WHERE table_schema = %s""", ('public',))
            tables = 0;
            for (table,schema) in cur.fetchall():
                tables = tables + 1
#                print(table)
#                print(schema)
            if tables != 0:
                cur.close()
                return
            #Can't use \i so this horrible parsing code instead
            with open('database/schema.psql', 'r') as inp:
                cmd = ''
                for line in inp:
                    line = line.rstrip('\r\n')
                    line = line.rstrip('\n')
                    if line.startswith('--'):
                        pass
                    elif line.startswith(' '):
                        cmd = cmd + line
                    elif line.endswith(';'):
                        cmd = cmd + line
                        print(cmd)
                        cur.execute(cmd)
                        conn.commit()
                        cmd = ''
                    else:
                        cmd = cmd + line
            inp.close()
            cur.close()

