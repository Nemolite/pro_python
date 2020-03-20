class Test:
	terra = 1
	def myfun(self,chislo):
		self.inner = chislo
		print(self.inner)
#class Test

obj = Test() #объект
obj.myfun(11)
print(obj.terra)


obj1 =Test()
obj1.myfun(41)
print(obj1.terra)
obj1.terra = 11111111
print(obj1.terra)
obj1.news2 = 22
print(obj1.news2)

obj21 =Test()
obj21.myfun(118)
print(obj21.terra)

obj31 =Test()
obj31.myfun(211)
print(obj31.terra)


class Mycalss:
	mypolr = 1
	mypole2 = 2

b = Mycalss()
print(b.mypole2)
print(b.mypolr)


class Unit21:
	def hels(self,tel):
		sum = tel + 20
		print(sum)

verti = Unit21()
verti.hels(12)



