print "";
num1 = float (input('Ingrese su primer numero'))
num2 = float (input('Ingrese su segundo numero'))
num3 = float (input('Ingrese su tercer numero'))

if num2 < num1 > num3:
	print ("El numero mayor es el primer numero. Numero:", num1)
elif num1 < num2 > num3:
	print ("El numero mayor es el segundo numero. Numero:", num2)
elif num1 < num3 > num2:
	print ("El numero mayor es el segundo numero. Numero:", num3)