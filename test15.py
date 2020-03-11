sp1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
sp2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nw_sp1 = sp1[::3]
nw_sp2 = sp2[::2]
print("====")
print(len(nw_sp2))
print("====")

i = 0
while i<=len(nw_sp2):
	if i>= len(nw_sp1):
		nw_sp1.append(0)
	print(nw_sp1[i] + nw_sp2[i]," ==",i)
	i = i+1

	if i==len(nw_sp2):
		break


    	


