slovar = {'key1':'test1','key2':'obj3','ret':'1234'}
print(slovar)

mas=[('key1','var1'),('key2','var2')]
print(mas)
slv2 = dict(mas)
print(slv2)

new1 = slv2['key1']
print(new1)
print(slv2['key2'])
print(slovar['ret'])
fart = dict([('key11','var11'),('key21','var2')])
print(fart)
fart['tkey'] = 'new_var'
print(fart)

empy = {}
print(empy)
empy['n1'] ='v2'
print(empy)

scan1 = 'n2' in empy
if scan1:
	print(scan1) 
else:
	print(' not')
for vname in slovar:
	print(vname)

for value in slovar.values():
	print(value) 
print("--------------")
for key21, value21 in slovar.items():
	print(key21,value21)
del slovar['key2']
print(slovar)
for vname in slovar:
	print(vname)

