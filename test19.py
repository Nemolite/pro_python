n = 5
i=2
a = [1,2]
print(a)
print(a[i-2])
print(a[i-1])
while i<n:

	a.append(a[i-2] + a[i-1])
	i = i + 1

print(a)

summa=0
for element in a:
	if element%2==0:
		summa = summa + element

print(summa)		

