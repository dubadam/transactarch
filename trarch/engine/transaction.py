from datetime import datetime


class Transaction:

    tablename = 'transaction'

    def __init__(self, user_id, cursor):
        self.user = user_id
        self.date = datetime.now()
        self.cursor = cursor
        self._id = False

    @property
    def status(self):
        return isinstance(self._id, int)

    def start(self):
        query = "INSERT INTO " + self.tablename + "(user_id, date) VALUES(%s, %s) RETURNING id;"
        self.cursor.execute(query, (self.user, self.date))
        self._id = self.cursor.fetchone()[0]

    def reset(self):
        del self._id

    @property
    def id(self):
        return self._id
