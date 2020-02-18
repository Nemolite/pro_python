names = ['str1','str2','str3','str4']
print(names)
name_to_rev = []
for name in names:
	if name not in ['str3','str4']:
		name_to_rev.append(name)

for name in name_to_rev:
	names.remove(name)
print(names)

#while цикл
n = 5
while n>0:
	n = n - 1
	print(n)
print("----------")
m = 10
while m>0:
    m+=1
    print(m)
    if m == 100:
    	break
#Словари




	