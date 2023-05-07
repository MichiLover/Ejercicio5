class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = ''
    __cuota = ''
    __licitacion = ''

    #constructor de la lista
    def __init__(self,cod,mod,ver,val,cuota,lic):
        self.__codigo = int(cod)
        self.__modelo = mod
        self.__version = ver
        self.__valor = val
        self.__cuota = cuota
        self.__licitacion = lic
        

        print("Codigo del auto: {}".format(self.__codigo))
        print("Modelo del auto: {}".format(self.__modelo))
        print("Version del auto: {}".format(self.__version))
        print("Valor del auto: {}".format(self.__valor))
        print("Cant. de cuotas del auto: {}".format(self.__cuota))
        print("Cant. de cuotas para licitar el auto: {}".format(self.__licitacion))


    def show(self,cod,mod,ver,val,cuota,lic):
        self.__codigo = int(cod)
        self.__modelo = mod
        self.__version = ver
        self.__valor = val
        self.__cuota = cuota
        self.__licitacion = lic
        

        print("Codigo del auto: {}".format(self.__codigo))
        print("Modelo del auto: {}".format(self.__modelo))
        print("Version del auto: {}".format(self.__version))
        print("Valor del auto: {}".format(self.__valor))
        print("Cant. de cuotas del auto: {}".format(self.__cuota))
        print("Cant. de cuotas para licitar el auto: {}".format(self.__licitacion))

        
    def actualiza(self,newValor):
        self.__valor= newValor
        print("Valor actualizado")

    def mostrar(self):
        print(f"Codigo de plan: {self.__codigo}, Modelo: {self.__modelo}, Version: {self.__version} ")

    def calcularCuota(self,xvalor):
        valorcuota= int (self.__valor/self.__cuota) + (self.__valor * 0.10)
        return valorcuota

    def licitar(self):
        valorcuota= int (self.__valor/self.__cuota) + (self.__valor * 0.10)
        monto = int (self.__licitacion * valorcuota)
        return monto
       
    def newLicitacion(self,newLic):
        self.__licitacion = newLic
        print("Cantidad de cuotas para licitar actualizadas")

    def getCodigo(self):
        return self.__codigo
            
    def modificarCL(self, cantidad):
        self.__licitacion = cantidad
        print("Cantidad de cuotas para licitacion modificada con exito ")
