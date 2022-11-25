import datetime
from dbconnection import DBConnection
class SignupDAO:
   def insert_signup(self,user_id,first_name,last_name,email_address):
        dbconnection=DBConnection()
        connection=dbconnection.getconnection()
        cursor=connection.cursor()
        cursor.execute('''insert into sign_up(user_id,first_name,last_name,email_address) values(%s,%s,%s,%s);''',(user_id,first_name,last_name,email_address))
        connection.commit()
   def selectsignup(self):
        print('select operation')
        dbConnection=DBConnection()
        connection=dbConnection.getconnection()
        print('Sign_up')
        cursor=connection.cursor()
        statement='''select * from Sign_up;'''
        cursor.execute(statement)
        minutelist=cursor.fetchall()
        for r in minutelist:
            print(r)
   def update_signup(self,user_id,first_name,last_name,email_address):
        dbconnection=DBConnection()
        connection=dbconnection.getconnection()
        cursor=connection.cursor()
        cursor.execute('''update sign_up where ''',(user_id,first_name,last_name,email_address))
        connection.commit()
        connection.commit()
    
user_id= 101
first_name='Velmani'
last_name='Selvaraj'
email_address='vmani3479@gmail.com'
signupdao=SignupDAO()
signupdao.insert_signup(user_id,first_name,last_name,email_address)
signupdao.selectsignup()