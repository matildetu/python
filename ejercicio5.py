print "";
a=int(input("ingrese el primer numero \n"))
b=int(input("ingrese el segundo numero \n"))
c=int(input("ingrese el tercer numero \n"))
d=int(input("ingrese el cuarto numero \n"))

lista=(a,b,c,d)
lista1=(b,c,d,a)
lista2=(c,d,a,b)
lista3=(d,a,b,c,)

print ("los numeros de la lista ingresados son \n"+ str (lista))
print ("Rotacion 1 \n "+ str (lista1))
print ("Rotacion 2 \n "+ str (lista2))
print ("Rotacion 3 \n"+ str (lista3))
