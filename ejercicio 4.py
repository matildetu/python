
def mayor(a,b,c):

	may = ''

	if a > b:
		if a > c:
			may=a
	else:
		if b > a:
			if b > c:
				may=b
			else:
				may=c

	return may,a,b,c
mayornum, x , y , z = mayor(9,20,4)

print "de los numeros: " , x , " , " , y , " , " , z , " el numero mayor es: " , mayornum