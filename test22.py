cod2ip = {'а': '01',
          'б': '02',
          'в': '03',
          'г': '04',
          'д': '05',
          'е': '06',
          'ё': '07',
          'ж': '08',
          'з': '09',
          'и': '0A',
          'й': '0B',
          'к': '0C',
          'л': '0D',
          'м': '0E',
          'н': '0F',
          'о': '10',
          'п': '11',
          'р': '12',
          'с': '13',
          'т': '14',
          'у': '15',
          'ф': '16',
          'х': '17',
          'ц': '18',
          'ч': '19',
          'ш': '1A',
          'щ': '1B',
          'ъ': '1C',
          'ы': '1D',
          'ь': '1E',
          'э': '1F',
          'ю': '20',
          'я': '21',
          ' ': '22',

          }

examstr = input("Введите слова для кодирования=")
listexamstr = list(examstr)
innertxt = print(listexamstr)
res = [] 
def coding(txtarr):
	for keytxt in txtarr:
		print(keytxt)
		for kval,sval in cod2ip.items():
			if kval==keytxt:
				print(sval)
				res.append(sval)
				break
coding(listexamstr)
print(res)
myString = '-'.join(res)
print("Ваш код = ",myString)







