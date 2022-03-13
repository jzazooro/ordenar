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