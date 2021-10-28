import psycopg2

class DBConnector():
    def __init__(self):
        self.db = psycopg2.connect(host='localhost', dbname='agens',user='agens',password='agens',port=15432)
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

    def set_graph_path(self):
        graph_path = 'ag_graph'
        set_graph_path = f"SET graph_path ={graph_path}".format(graph_path=graph_path)
        self.cursor.execute(set_graph_path)
        print(f'graph path is selected : {graph_path}'.format(graph_path=graph_path))
