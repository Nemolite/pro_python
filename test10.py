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
   
        add_emp = ("INSERT INTO t "
               "(a, b)"
               "VALUES (%(a)s, %(b)s)")

        data_sal = {
            'a': 27,
            'b': 34,
            
        }
     
        cursor.execute(add_emp,data_sal)
        connection.commit()
      
           
finally:
    
    connection.close()