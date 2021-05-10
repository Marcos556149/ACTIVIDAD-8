from ClaseConjunto import Conjunto
if __name__=='__main__':
    print("TEST CONJUNTO\n")
    pruebaTest= Conjunto()
    pruebaTest.test()
    input()
    print("CREACION DEL CONJUNTO 1\n")
    conjunto1= Conjunto()
    num= 0
    verificar= str(input('Ingrese cualquier tecla si desea agregar un numero al conjunto 1, ingrese FIN para finalizar: '))
    while verificar != "FIN":
        num= int(input('Ingrese un numero para el primer conjunto, tiene que ser un numero que no halla sido ingresado previamente: '))
        if conjunto1.buscarNumero(num) == False:
            conjunto1.agregarNumero(num)
            verificar= str(input('Ingrese cualquier tecla si desea agregar un numero al conjunto 1, ingrese FIN para finalizar: '))
        else:
            verificar= str(input('El numero ingresado ya pertenece al conjunto, ingrese cualquier tecla si desea agregar un numero al conjunto 1, ingrese FIN para finalizar: '))
    print("\nCREACION DEL CONJUNTO 2\n")
    conjunto2= Conjunto()
    verificar= str(input('Ingrese cualquier tecla si desea agregar un numero al conjunto 2, ingrese FIN para finalizar: '))
    while verificar != "FIN":
        num= int(input('Ingrese un numero para el segundo conjunto, tiene que ser un numero que no halla sido ingresado previamente: '))
        if conjunto2.buscarNumero(num) == False:
            conjunto2.agregarNumero(num)
            verificar= str(input('Ingrese cualquier tecla si desea agregar un numero al conjunto 2, ingrese FIN para finalizar: '))
        else:
            verificar= str(input('El numero ingresado ya pertenece al conjunto, ingrese cualquier tecla si desea agragar un numero al conjunto 2, ingrese FIN para finalizar: '))
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Sumar dos conjuntos")
        print("[2]...Restar dos conjuntos")
        print("[3]...Verificar si los dos conjuntos son iguales")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(4):
                if op == 1:
                    suma= conjunto1 + conjunto2
                    suma.mostrar()
                if op == 2:
                    resta= conjunto1 - conjunto2
                    resta.mostrar()
                if op == 3:
                    if (conjunto1 == conjunto2):
                        print("\nLos dos conjuntos son iguales")
                    else:
                        print("\nLos dos conjuntos no son iguales")
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 3")
        except ValueError:
            print("ERROR, ingrese solamente numeros")

