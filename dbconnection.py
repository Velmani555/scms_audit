import mysql.connector
from mysql.connector import Error
class DBConnection:
    def getconnection(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='scms_audit',
                                         user='root',
                                         password='Bujji13042018*')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchall()
                print("You're connected to database: ", record)
                return connection

        except Error as e:
                print("Error while connecting to MySQL", e)
        
dbconnection=DBConnection()
dbconnection.getconnection()