names = ['str1','str2','str3','str4']
print(names)
name_to_rev = []
for name in names:
	if name not in ['str3','str4']:
		name_to_rev.append(name)

for name in name_to_rev:
	names.remove(name)
print(names)