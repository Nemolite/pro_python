#Новая задача
arr_spisok = [3,9,2,4,1,-2,-5,-3,0,2,4,7]
r = 0
for inx in range(len(arr_spisok)):
	r = r + arr_spisok[inx]
print(r)
#print(len(arr_spisok))
r1 = 0
print("=====================")
for in2 in arr_spisok:
	#print(in2)
	r1 = r1 + in2
print(r1)
print("=====================")

r2 = 0
i = 0
while i<len(arr_spisok):
    r2 = r2 + arr_spisok[i]
    i = i + 1
print(r2)

print("=====================")
r3 = 0
flag = True
im = 0
while flag:
    r3 = r3 + arr_spisok[im]
    #print(im)
    im = im + 1
    if im>len(arr_spisok)-1:
    	flag = False
print(r3)
print("=====================")
bidlo_result = 0
bidlo_result = arr_spisok[0]+arr_spisok[1]+arr_spisok[2]+arr_spisok[3]+arr_spisok[4]+arr_spisok[5]+arr_spisok[6]+arr_spisok[7]+arr_spisok[8]+arr_spisok[9]+arr_spisok[10]+arr_spisok[11]
print(bidlo_result)

print("************************************")
arr_spisok1 = [3,9,2,4,1,-2,-5,-3,0,2,4,7]
g=0
rg = 0
while g<5:
	for binex in range(len(arr_spisok1)):
		arr_spisok1[binex] = arr_spisok1[binex] + 1
		rg = rg + arr_spisok1[binex]
	print('Цикл==',g,'Сумма ==',rg)
	g = g + 1	
print(arr_spisok1)
print(rg)

#Применение циклов  


	
