import pprint
band1_names = ['John', 'George','Paul', 'Ringo'] 
band2_names = ['Paul'] 
names_to_bands = {}
for n4 in band1_names:
	names_to_bands.setdefault(n4,[]).append('Beatles')
for n5 in band2_names:
	names_to_bands.setdefault(n5,[]).append('Wings')	

pprint.pprint(names_to_bands, width=15)
