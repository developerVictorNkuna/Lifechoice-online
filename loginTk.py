import pymysql.cursors
from getpass import  getpass
# from pymysql.cursors import 
from tkinter import*
from pymysql.cursors import err



#connect to the databae


class Connect:
    def __init__(self,host,user,password,database):
        super().__init__()
        self.host =host
        self.user = user
        self.password = password
        self.database = database

    def create_Server_Connection(self,host,user,password,database):
        connection = None
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="lifechoices ​online",
                cursorclass=pymysql.cursors.DictCursor)
            print("MySQL Database Server connection is successfully established:")

        except err as Error:
            
            print(f"Error:'{Error}'")
        return connection




# with connection.cursor() as cursor:

#                     connection.commit()
#                     connection.close()



# # sql3 = "CREATE TABLE 'users'('id' int(11) NOT NULL AUTO_INCREMENT,'full_name' varchar(60) DEFAULT NULL,'username' varchar(50) DEFAULT NULL,'password' varchar(20) DEFAULT NULL,PRIMARY KEY ('id'));"
# # connect =Connect("localhost","root","","lifechoices online")
    


