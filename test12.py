import pymysql.cursors 
# Функция подключения к базе данных.
def condb():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='basaspisok',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
    return connection 
#Модуль  вывода списка
def viewsipok(podkluch):
    print(11)
    try:
        with podkluch.cursor() as cursor:
            sele = ("SELECT * FROM spisok")
            cursor.execute(sele)
            print ("cursor.description: ", cursor.description)
            print()
            for row in cursor:
                print(row)
    finally:
        podkluch.close() 
#Модуль внесения данных в бд


  
#Создаем пользовательский интерфейс
flag = False
while flag == False:
    print("Выберите варианы")
    print("Вывести список - 1")
    print("Внести изменения в список - 2")
    print("Выход - 0")
    slot = int(input("Ваш выбор ="))
    print(slot)
    if slot == 0:
        print("Программа завершила свое выполнение")
        break
    if (slot not in [1,2]):
        print("Возможно вы ошиблись, повторите ввод")
        continue
    if slot == 1:
        print(1)
        con = condb() 
        viewsipok(con)
    if slot == 2:
        print(2)
        #модуль внесения 



