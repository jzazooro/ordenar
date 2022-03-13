from ejercicios.ejercicio1 import primerejercicioa
from ejercicios.ejercicio1 import primerejerciciob
from ejercicios.ejercicio2 import segundoejercicio
from ejercicios.ejercicio3 import tercerejercicio
if __name__=="__main__":
    while True:
        enunciado=int(input("¿Que ejercicio deseas ejecutar?: "))
        if enunciado==1:
            ejercicioa=primerejercicioa()
            ejerciciob=primerejerciciob()
        if enunciado==2:
            ejercicio=segundoejercicio()
            ejercicio.ordenacion(1, 0)
        if enunciado==3:
            ejercicio=tercerejercicio()