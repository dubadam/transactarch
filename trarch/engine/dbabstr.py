from transaction import Transaction
import psycopg2


class Storage:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=test user=postgres")
        self.cursor = self.conn.cursor()
        self.t = Transaction(1, self.cursor)