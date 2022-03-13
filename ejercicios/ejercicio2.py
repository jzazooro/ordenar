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