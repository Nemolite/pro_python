vari = 20

print("---------1----------")
def add2(num1,num2):
	sum2 = num1+num2
	return sum2
res = add2(2,2)
print(res)
print("---------2----------")

def add3(num1,num2):
	sum2 = num1+num2
	print(sum2)
add3(2,2)
print("---------3---------")

def add4(num1,num2):
	print(num1+num2)
add4(2,2)
print("---------4---------")

def selt(n1,n2 = 2):
	print(n1 + n2)
	
selt(2,3)
selt(2)
print("---------5---------")

def selt2(n1,n2,n3):
	print(n1 + n2 + n3 + vari)
	
selt2(2,3,2)

print("---------6---------")
spi = ['qwe',123,'444',45]

def selt3(spiexam):
	#print(spiexam)
	a = 123
	for ver1 in spiexam:
		if a == ver1:
			fl = True
			break
		else:
			fl = False

	if fl == False:
		return -1
	else:
		return 1

ff = selt3(spi)
print(ff)

