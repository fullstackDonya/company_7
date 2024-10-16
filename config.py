import mysql.connector

def connect_to_db():
    conn = mysql.connector.connect(
        host="mysql-compagny.alwaysdata.net",     
        user="compagny_miguel",       
        password="Miguel2024",  
        database="compagny_gp_7",     
        port=3306,  
        use_pure=True
    )
    return conn
