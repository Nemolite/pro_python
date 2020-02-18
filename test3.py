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
    if m == 17:
    	break
#Словари
info_slovo = dict(n1=25,n2='dfr',n4=True)
print(info_slovo)
print(info_slovo['n1'])

info_slovo1 = dict([('f1',24),('f2','stop')])
print(info_slovo1)
info_slovo['n3'] =False
if info_slovo['n3'] == True:
	print(True)
else:
	print(False)

genre = info_slovo1.get('Genre', 'Rock')
print(genre)
print(info_slovo1)





	