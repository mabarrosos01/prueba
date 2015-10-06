import pdb

palabras=["xtl" ,"xml" , "xd" , "abc" , "snt" , "drl"]
lx=[]
ls=[]
for palabra in palabras: 
	if palabras[0] == "x":
		lx.append(palabra)
	else:
		ls.append(palabra)
		
lista_final = sorted(lx)+sorted(ls)
print lista_final


