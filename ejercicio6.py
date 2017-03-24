
--6. Realiza un programa que permita generar un intervalo de la suma de los cubos de los primeros n números. 

def interSuma(x):      
        a = [( cont ** 3 )  for cont in range( 1 , x + 1 )]        
        print a
        return sum(a)