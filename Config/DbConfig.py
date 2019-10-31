import pymysql.cursors
from flask import jsonify

class DbConfig():
    
    def __init__(self):
        self.connection()
  
    def connection(self):
        conn = pymysql.connect("localhost", "root","root", "softporc")
        return conn
    
    def delete(self, query):
        try:
            c = self.connection().cursor()
            c.execute(query)
            self.connection().commit()
            return jsonify({"messaje": "200"})
        except Exception as e:
            return e
        
        self.close()
             
    def read(self, query):
        try:
            c = self.connection().cursor()
            c.execute(query)
            return  jsonify(data=c.fetchall())        
        except Exception as e:
            return e
        self.close()
        
    def update(self, query):
        conne = pymysql.connect("localhost", "root","root", "softporc")
        try:
            with self.connection().cursor() as cursor:
                cursor.execute(query)
            self.connection().commit()
            return "ok"
        except Exception as e:
            return e
        
        finally:
            self.close()
            
    def insert(self, query):
        conn = pymysql.connect("localhost", "root","root", "softporc")
        try: 
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            
        finally:
            self.close()
        
    def close(self):
        self.connection().close()