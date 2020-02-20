#Еще раз про словари
names = ['Ringo','Paul','John','Ringo']
count = {}
for name in names:
	count.setdefault(name, 0)
	count[name]= count[name] + 1
print(count)

c2 = {}
for n1 in names:
	if n1 not in c2:
		c2[n1] = 1
	else:
		c2[n1] += 1
print(c2)		
