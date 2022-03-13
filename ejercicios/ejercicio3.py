class tercerejercicio():
    def __init__(self, tabla):
        self.tabla=list(tabla)
    def seleccionarsegmento(self, max, min):
        max=int(input("¿cual quieres que sea el limite superior?: "))
        min=int(input("¿cual quieres que sea el limite inferior?: "))
    def obtenermax(self, tabla, max, min):
        for i in range(min, max):
            maximo=self.tabla[i]
    def desplazar(self, tabla, max, min):
        for i in range(min, (max-1)):
            self.tabla[i]=self.tabla[i+1]
        return self.tabla