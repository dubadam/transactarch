from datetime import datetime


class Transaction:

    tablename = 'transaction'

    def __init__(self, user_id, cursor):
        self.user = user_id
        self.date = datetime.now()
        self.cursor = cursor

    def start(self):
        query = "INSERT INTO " + self.tablename + "(user_id, date) VALUES(%s, %s) RETURNING id;"
        self.cursor.execute(query, (self.user, self.date))
        self._id = self.cursor.fetchone()[0]