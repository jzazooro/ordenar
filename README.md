# ordenar

Mi direccion de github para este repositorio es la siguiente: [GitHub](https://github.com/jzazooro/ordenar.git)
https://github.com/jzazooro/ordenar.git

Hemos resuelto los ejercicios: 1.ordenacion por insercion dicotomica, 2.una ordenacion topologica, 3.completar las especificaciones. Para eso hemos usado clases en todos los ejercicios.

El diagrama de flujo que tenemos en nuestro codigo es el siguiente: 

![diagrama de flujo ordenar](https://github.com/jzazooro/ordenar/blob/main/diagramadeflujo.jpg)

Main

```
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
```

Ejercicio 1. Ordenacion por insercion dicotomica

```
class primerejercicioa:
    def __init__(self, tabla):
        self.tabla=tabla
    def ordenarlatabla(self):
        self.tabla.sort()
        return self.tabla
class primerejerciciob:
    def __init__(self, tabla):
        primerejercicioa.__init__(self, tabla)
        n=[]
        self.n=n
    def ordenarlistavacia(self):
        primerejercicioa.ordenar(self)
        for i in self.tabla:
            self.n.append(i)
        return self.n
```

Ejercicio 2. Una ordenacion dicotomica

```
import random
class segundoejercicio(): 
    def __init__(self):
        tareas=[]
        for i in range:
            (int(input("¿cuantas tareas va a realizar?: ")))
            tarea= 't'+(str(i+1))
            tareas.append(tarea)
        random.shuffle(tareas)
        print(tareas)
        ordenacion=[]
        self.tareas=tareas
        self.ordenacion=ordenacion
    def ordenacion(self, k, t): 
        if len(self.tareas)>0:
            if't'+str(k)==self.tareas[t]:
                print("se ha realizado la tarea", k)
                self.orden.append(self.tareas[t])
                del self.tareas[t]
                self.ordenacion(k+1, 0)
            else:
                print("esa no es la tarea que tiene que realiar, haz la tarea", k)
        else:
            print(self.orden)
```

Ejercicio 3. Completar las especificaciones

```

```
