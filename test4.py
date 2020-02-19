set_info = [2,4,6,-2,-3,-7,8,11,23,45]
#Каждый из элеметов увеличиваем 1
#и каждый раз проверяем сумму всех 
#элементов.
#если число стало 78947, то выходим из цикла
result2 = 0
while result2 < 78947:
	#Находим сумму
	for index in range(len(set_info)): 	
		set_info[index] = set_info[index] + 1
	for var1 in set_info:
		result2 = result2 + var1
print(set_info)
print("-----------------")
print(result2)







	
