from transaction import Transaction
import psycopg2


class Storage:
    def __init__(self):
        self.t = Transaction(1)