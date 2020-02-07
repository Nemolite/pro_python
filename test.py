terra = ('one','two')
print(terra)
notempty = tuple(['three','four']) 
print(notempty)
print(notempty[0])
a = tuple('hello, world!')
print(a)
print(a[7],a[8])

n = tuple('t',) 
print(n)

p = 'Steph','Curry','Guard' 
print(p)
digi = [1,2,3,4,5,1]
mno_digi = set(digi)
print(mno_digi)
flag = (13 in mno_digi)
print(flag)

odd = {1, 3, 5, 7, 9}
print(odd)

main_var = odd - mno_digi
print(main_var)
main_var1 = mno_digi - odd
print(main_var1)

m1 = mno_digi & odd
print(m1)

nab = mno_digi | odd
print(nab)

iskl = mno_digi ^ odd
print(iskl)
