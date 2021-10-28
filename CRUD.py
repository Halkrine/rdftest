from DBConnector import DBConnector

class CRUD(DBConnector):
    def insertDB(self,schema,table,colum,data):
        sql = " INSERT INTO {schema}.{table}({colum}) VALUES ('{data}') ;".format(schema=schema,table=table,colum=colum,data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" insert DB err ",e)

    def readDB(self,schema,table,colum):
        sql = " SELECT {colum} from {schema}.{table}".format(colum=colum,schema=schema,table=table)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)

        return result

    def updateDB(self,schema,table,colum,value,condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema
                                                                                                   , table=table , colum=colum ,value=value,condition=condition )
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" update DB err",e)

    def deleteDB(self,schema,table,condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema,table=table,
                                                                          condition=condition)
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print( "delete DB err", e)

    def setGraphPath(self,path):
        sql = " set graph_path = {path}".format(path=path)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("match Error : ", e)

    def matchDB(self,alias,node,condition,returnAlias):
        sql = """ 
            match (v:v_test)-[e]->(n) 
            where {condition} return {returnAlias};
        
        """.format(alias=alias,node=node,condition=condition,returnAlias=returnAlias)

        try:
            print(sql)
            self.cursor.execute(sql)
            self.db.commit()
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print("match Error : ", e)

if __name__ == "__main__":
    db = CRUD()
    db.set_graph_path()
  #  db.insertDB(schema='myschema',table='table',colum='ID',data='유동적변경')
 #   print(db.readDB(schema='ag_graph',table='v_vertest',colum='ID,properties'))
    print(db.setGraphPath(path='ag_graph'))
    print(db.matchDB(alias='v',node='v_test',condition='1=1', returnAlias='v,e,n'))
   # db.updateDB(schema='myschema',table='table',colum='ID', value='와우',condition='유동적변경')
   # db.deleteDB(schema='myschema',table='table',condition ="id != 'd'")