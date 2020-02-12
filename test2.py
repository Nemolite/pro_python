for it_is_may_var in [2,3,4,5,6,7,]:
	print(it_is_may_var)
	print(it_is_may_var*2)
	a = it_is_may_var + 20
print("--------------------")	
print(a)

print("---------This is new a programm-----------")	

dig = ["set1","waef","qwe","qwe"]
for it333 in dig:
	print(it333)

print("---------This is new a programm ver 2-----------")	
for adr in range(len(dig)):
	print(adr,"=",dig[adr])

print("---------This is new a programm ver3-----------")	
automobil = ["volga","moskvich","jiguli","zaparojez"]
for one_auto_index,one_auto_var in enumerate(automobil):
	print(one_auto_index,"==",one_auto_var)


print("---------This is example -----------")	

dano = [2,7,8,11,12,3,-1,0,4,-2,5,21]
#Найти сумму чисел больше 10
#Найти произведение чисел меньше 10 
#Отрицательные числа в расчет не принимать
res_summ = 0
res_proiz = 1
for chislo in dano:
	if chislo>10:
		res_summ+=chislo
	if (chislo<10)and(chislo>0):
		res_proiz = res_proiz * chislo
print(res_summ)	
print(res_proiz)	
