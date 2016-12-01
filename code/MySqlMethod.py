import pymysql
import confidentials

class MySqlMethod:
    def __init__(self):
        secrets=confidentials.getMySqlAuth()
        conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
        cur=conn.cursor()
    
    def insertData(self,sql):
        cur.execute(sql)
        return cur.lastrowdid