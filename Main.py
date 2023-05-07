import csv
from ManejadorPlanes import PlanAhorro

if __name__ == "__main__":
    print("EJERCICIO 1")
    newPlan = [] #creo la lista para guardar los datos
    archivo = open('planes.csv')
    reader= csv.reader(archivo,delimiter=(';'))
    for fila in reader:
        codigo=int(fila[0])
        modelo=fila[1]
        version=fila[2]
        valor=int(fila[3])
        cuota=int(fila[4])
        pagas=int(fila[5])

        plan=PlanAhorro(codigo,modelo,version,valor,cuota,pagas)
        newPlan.append(plan)
        print("\n")
    archivo.close()
    print("--------------------------------------------------------------------")

    menu = input("Elegir opcion: \n a- Actualizar el valor del vehiculo de cada plan\n b- Ingresar un valor\n c-Mostrar el monto pagado para licitar el vehiculo\n d-Modificar cant. de cuotas pagas para licitar\n")
    while menu != "z":
        if menu == "a":
            for i in range(len(newPlan)):
                newPlan[i].mostrar()
                xvalor= int(input("Ingresar el nuevo valor para el vehiculo {}: ".format(i+1)))
                newPlan[i].actualiza(xvalor)
        elif menu == "b":
            newvalor = int(input("Ingresar un valor: "))
            for i in range(len(newPlan)):
                calculo = newPlan[i].calcularCuota(newvalor) #Calculo el valor de la cuota de ese plan i
                if newvalor > calculo:
                    print("\n")
                    print("Se muestran los planes que el valor de la cuota es menor al valor ingresado")
                    newPlan[i].mostrar()
                else:
                    print("Plan {}".format(i+1))
                    print("El valor ingresado es menor que el valor de la cuota")
        elif menu == "c":
            for i in range(len(newPlan)):
                monto=newPlan[i].licitar()
                print("Para licitar el vehiculo {},se debe abonar un monto de {} pesos".format(i+1,monto))

        elif menu == "d":
            cod = int(input("Ingrese el codigo del plan al que le quiere cambiar la cantidad de cuotas de licitacion: "))
            for i in range(len(newPlan)):
                if cod == newPlan[i].getCodigo():
                    print("El plan es:")
                    newPlan[i].mostrar()
                    cant = int(input("Ingrese la nueva cantidad de cuotas para licitacion: "))
                    newPlan[i].modificarCL(cant)
                    newPlan[i].show(codigo,modelo,version,valor,cuota,cant)
        else:
            print("Opcion incorrecta, presione z para salir")

        menu = input("Elegir opcion: \n a- Actualizar el valor del vehiculo de cada plan\n b- Ingresar un valor\n c-Mostrar el monto pagado para licitar el vehiculo\n d-Modificar cant. de cuotas pagas para licitar\n")    