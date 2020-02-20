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
import collections
c3 = collections.Counter(names)
print(c3)

band1_names = ['John', 'George','Paul', 'Ringo'] 
band2_names = ['Paul'] 
names_to_bands = {}
for n4 in band1_names:
	names_to_bands.setdefault(n4,[].append('Beatles'))
for n5 in band2_names:
	names_to_bands.setdefault(n4,[].append('Wings'))	
print(band1_names)
print(band2_names)
print(names_to_bands['Paul'])