def intercala(x):

	n=x
	impares=''
	while n <= 31:
		if n%2 !=0:
			impares+='%i, ' % n
		n+=1
	return n, impares

numero, lista = intercala(13)

print "lista Numeros impares : ", lista