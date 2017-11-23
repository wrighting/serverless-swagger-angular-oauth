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

        database_name = os.getenv('DATABASE','example'),
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
                print('1')
                self._logger.exception("Database connection problem")
                print('1a')
                config['database'] = 'postgres'
                print('1b')
                conn = psycopg2.connect(connection_factory=LoggingConnection, **config )
                print('1c')
                conn.initialize(self._logger)
                print('1d')
                cur = conn.cursor()
                print('CREATE DATABASE ' + database_name)
                cur.execute('CREATE DATABASE ' + database_name)
                print('1e')
                cur.close()
                conn.close()
                self._tries = self._tries + 1
                if self._tries < 2:
                    return self._init_connection()
                else:
                    return None

            if os.getenv('CREATE_SCHEMA_IF_MISSING', "false") == "true":
                print('2')
                cur = conn.cursor()
                cur.execute("SET search_path TO " + database_name + ',public,contrib')
                cur.execute("\d")
                res = cur.fetchone()
                if not res:
                    cur.execute("\i database/schema.psql")

                cur.close()
        except Exception as e:
            print('3')
            self._logger.exception("Database connection problem")

        return conn

