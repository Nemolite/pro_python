count_names=['test1','test2']
print(count_names)

other_names = list(['Fred', 'Charles']) 
print(other_names)
#Добавление элемента в конец списка
other_names.append('Matt') 
print(other_names)
#Добавление элемента в конец списка
count_names.append('Matt3')	
print(count_names)
#Сливание двух спсиков
count_names.extend(other_names)
print(count_names)
#'set' вписываем в список вторым
count_names.insert(2,'set')
print(count_names)
