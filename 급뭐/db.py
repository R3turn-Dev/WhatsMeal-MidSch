from psycopg2 import connect
from threading import get_ident


class DBManager:
    def __init__(self, config):
        self.conn = None
        self.cursor = None

        self.connDict = {}
        self.curDict = {}

        self.host = config.host
        self.port = config.post
        self.db = config.db
        self.user = config.user
        self.pw = config.pw

    def getConn(self):
        self.conn = connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pw,
            database=self.db
        )

        self.conn.autocommit = True
        return self.conn

    def getCursor(self):
        thread_id = get_ident().__int__()

        if thread_id not in self.connDict.keys():
            self.connDict[thread_id] = self.getConn()

        if thread_id not in self.curDict.keys():
            self.curDict[thread_id] = self.connDict[thread_id].cursor()

        return self.curDict[thread_id]

    def execute(self, query):
        return self.getConn().execute(query)
