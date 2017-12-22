from datetime import datetime
import psycopg2

class Transaction:

    tablename = 'transaction'

    def __init__(self, user_id):
        self.user = user_id
        self.date = datetime.now()
        self.conn = psycopg2.connect("dbname=test user=postgres")
        self.cursor = self.conn.cursor()
        self._id = False

    @property
    def status(self):
        return isinstance(self._id, int)

    @property
    def id(self):
        return self._id

    def start(self):
        query = "INSERT INTO " + self.tablename + "(user_id, date) VALUES(%s, %s) RETURNING id;"
        self.cursor.execute(query, (self.user, self.date))
        self._id = self.cursor.fetchone()[0]

    def reset(self):
        self.conn.rollback()
        del self._id

    def commit(self):
        self.conn.commit()
        self.start()

    def process_query(self, query, data):
        self.cursor.execute(query, data)
        return self.cursor.fetchall()