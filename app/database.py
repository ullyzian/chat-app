import psycopg2
import logging
import sys


class Database():
    """Database class to connect, run queries and insert data to Postgres"""

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.conn = None

    def open_connection(self):
        try:
            if (self.conn is None):
                self.conn = psycopg2.connect(user=self.user, password=self.password,
                                             host=self.host, port=self.port, database=self.database)
        except psycopg2.DatabaseError as e:
            logging.error(e)
            sys.exit()
        finally:
            logging.info("Connection opened successfully.")

    def run_query(self, query, *args):
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'SELECT' in query:
                    records = []
                    cur.execute(query, *args)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records
                else:
                    result = cur.execute(query, *args)
                    self.conn.commit()
                    affected = f"{cur.rowcount} rows affected"
                    cur.close()
                    return affected
        except psycopg2.DatabaseError as e:
            print(e)

    def create_tables(self, commands):
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                self.conn.commit()
                cur.close()

        except psycopg2.DatabaseError as e:
            print(e)
        finally:
            if self.conn:
                self.conn.close()
                logging.info("Database connection closed.")
