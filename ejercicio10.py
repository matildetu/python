def sumaRecursivaNumerosCuadrados(n):

if (n==1):

    return 1
else
    return n*n+ sumaRecursivaNumerosCuadrados(n-1)

n=int(input("cantidad de terminos ciadrados a sumar: "))

print ("la suma de los cuadrados  es: " + str (sumaRecursivaNumerosCuadrados(n)))
