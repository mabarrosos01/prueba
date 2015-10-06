numeros=[1,2,4,4,5,6,5,7,7,8,9,9,11,11,13,17,17,32,45,52]
resultado = []
for indice,elemento in enumerate(numeros):
	if indice != len(numeros) -1:
		if elemento != numeros[indice +1]:
			resultado.append(elemento)

resultado.append(numeros[-1])
print resultado
