class Conjunto:
    __elementos= []
    def __init__(self,conjuntoo= None):
        if conjuntoo == None:
            self.__elementos= []
        else:
            self.__elementos= conjuntoo
    def test(self):
        self.__elementos.append(1)
        self.__elementos.append(9)
        self.__elementos.append(3)
        self.__elementos.append(10)
        self.__elementos.append(5)
        self.mostrar()
        print("\nTEST REALIZADO EXITOSAMENTE\n")
    def mostrar(self):
        print(self.__elementos)
    def getConjunto(self):
        return self.__elementos
    def getNumero(self,indice):
        return self.__elementos[indice]
    def agregarNumero(self,num):
        self.__elementos.append(num)
    def buscarNumero(self,numm):
        return numm in self.__elementos
    def __add__(self,otro):
        listaResultadoSuma= []
        for z in range(len(otro.getConjunto())):
            listaResultadoSuma.append(otro.getNumero(z))
        for i in range(len(self.__elementos)):
            if (self.__elementos[i] in listaResultadoSuma) == False:
                listaResultadoSuma.append(self.__elementos[i])
        return Conjunto(listaResultadoSuma)
    def __sub__(self,otro1):
        listaResultadoResta= []
        for j in range(len(self.__elementos)):
            if otro1.buscarNumero(self.__elementos[j]) == False:
                listaResultadoResta.append(self.__elementos[j])
        return Conjunto(listaResultadoResta)
    def __eq__(self,otro2):
        bandera= True
        longitudOtro2= len(otro2.getConjunto())
        i=0
        if len(self.__elementos) == longitudOtro2:
            print
            while (bandera)and(i < longitudOtro2):
                if (otro2.buscarNumero(self.__elementos[i]) == False):
                    bandera= False
                i += 1
        else:
            bandera= False
        return bandera
