import psycopg2

class DBConnector():
    def __init__(self):
        self.db = psycopg2.connect(host='localhost', dbname='test',user='test',password='test',port=5432)

        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()