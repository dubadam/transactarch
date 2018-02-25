class Repository:

    tablename = 'repo'

    def __init__(self, storage):
        self._storage = storage
        self._valid = False
        self._id = False
        self._guid = False
