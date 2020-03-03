import pymysql.cursors  

# Подключиться к базе данных.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='test3',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
 
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT * FROM one "
         
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
 
        for row in cursor:
            print(row)
             
finally:
    # Закрыть соединение (Close connection).      
    connection.close()