radio = input('Ingrese el valor del radio de la esfera')
radio=int(radio)

def rad(radio):
	cubo=radio**3
	vol=4/3*(3.1416*(radio**3))
	print ("el radio de la esfera es")
	print (vol)

rad(radio)