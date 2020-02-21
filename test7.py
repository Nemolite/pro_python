s2 = {'k1':[2,3,4],'k2':[11,12,13],'k3':[7,8,9]}
print(s2)
r = 0
for key,val in s2.items():
	for v1 in val:
		r = r + v1
	print(key,r)
