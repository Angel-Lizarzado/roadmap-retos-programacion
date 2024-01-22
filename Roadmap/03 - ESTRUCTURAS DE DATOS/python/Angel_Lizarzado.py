agenda = []
opcion = 0
def menu():
    # Mostrar las opciones
    print("Bienvenido a la agenda")
    print("1. Crear un contacto")
    print("2. Eliminar un contacto")
    print("3. Buscar un contacto")
    print("4. Actualizar un contacto")
    print("5. Consultar contactos")
    print("6. Salir")
    # Pedir al usuario que ingrese un número
    opcion = int(input("Ingrese el número de la opción que desea realizar: "))
    # Devolver la opción elegida
    return opcion


def create(nombre, numero):
    crear_contacto = {f"nombre" : nombre, "telefono" : numero}
    agenda.append(crear_contacto)

    return print(f"agregado {agenda}")

def delete(nombre):
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            agenda.remove(contacto)
            

def find (nombre):
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            print(f"Datos de contacto: {contacto['nombre']}, {contacto['telefono']}")

def consultar():
        print("Datos de contacto:")
        for contacto in agenda:
            print(contacto['nombre'])
            

def update(nombre):
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            telefono = contacto['telefono']
            print(f'Los datos de contacto son = Nombre: {nombre}, Telefono: {telefono}')
            act = int(input("Que dato desea actualizar? 1) Nombre  2) Telefono o escriba 3 para salir:  "))
            if act == 1:
                n = input("Ingrese el nuevo nombre: ")
                contacto["nombre"] = n
            elif act == 2:
                t = input("Ingrese el nuevo telefono: ")
                contacto["telefono"] = t
            elif act == 3:
                break
            else:
                print("Introduzca opcion valida")




if __name__ == "__main__":
    # Llamar al bucle
    while True:
        # Llamar a la función menu y guardar la opción
        opcion = menu()
        # Evaluar la opción
        if opcion == 1:
            # Llamar a la función create
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el número del contacto: ")
            create(nombre, numero)
            print("Contacto creado.")
        elif opcion == 2:
            # Llamar a la función delete
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            delete(nombre)
            input("Presione enter para continuar")
        elif opcion == 3:
            # Llamar a la función find
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            find(nombre)
            input("Presione enter para continuar")
        elif opcion == 4:
            # Llamar a la función update
            nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
            update(nombre)
            input("Presione enter para continuar")
        elif opcion == 5:
            # Llamar a la función update
            print("Tu agenda de contactos: ")
            consultar()
            input("Presione enter para continuar")
        elif opcion == 6:
            # Salir del programa
            print("Gracias por usar la agenda. Hasta pronto.")
            break
        else:
            # Mostrar un mensaje de error
            print("Opción inválida. Intente de nuevo.")
