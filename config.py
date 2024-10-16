import mysql.connector

def connect_to_db():
    conn = mysql.connector.connect(
        host="mysql-compagny.alwaysdata.net",     
        user="compagny",       
        password="Group7@!.",  
        database="compagny_gp_7",     
        port=3306                     
    )
    return conn
