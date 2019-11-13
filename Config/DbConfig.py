import pymysql
from flask import jsonify

class DbConfig():
                 
    def read(self, query):
        
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc",charset='utf8mb4')
        #conn = pymysql.connect("localhost","root","root", "softporc")
        try:
            c = conn.cursor()
            c.execute(query)
            return   c.fetchall()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return jsonify({'status': 400, 'Error': e}) 
        
        finally:
            conn.close()
        
    def update(self, query):
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc")
        #conn = pymysql.connect("localhost","root","root", "softporc")
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return jsonify({'status': 200})
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	        return jsonify({'status': 400, 'error': e})
        finally:
            conn.close()
                
    def insert(self, query):
        
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc")
        #conn = pymysql.connect("localhost","root","root", "softporc")
        
        try: 
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            
            return jsonify({'status': 200})
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return jsonify({'status': 400, 'Error': e}) 
        
        finally:
            conn.close()
            
    def delete(self, query):
        
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc")
        #conn = pymysql.connect("localhost","root","root", "softporc")
        
        try:
            c = conn.cursor()
            c.execute(query)
            conn.commit()
            return jsonify({"status": "200"})
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return jsonify({'status': 400, 'Error': e}) 
        
        finally:
            conn.close()
    
    def count (self, query):
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc")
        try:
            c = conn.cursor()
            c.execute(query)
            return c.fetchone()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return jsonify({'status': 400, 'Error': e}) 
        
        finally:
            conn.close()

    def employee(self, query):
        conn = pymysql.connect("200.93.148.19",  "softporc","4052018", "softporc")
        try:
            c = conn.cursor()
            c.execute(query)
            return c.fetchone()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            return jsonify({'status': 400, 'Error': e}) 
        
        finally:
            conn.close()