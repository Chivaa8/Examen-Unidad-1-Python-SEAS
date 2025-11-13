# VARIABLES
fichero = "agenda.txt"
open(fichero, "a").close()  # crea el archivo si no existe

# FUNCIONES
def introducirNombre():
    nombre = input('Nombre del cliente: ').strip() #eliminamos algun espacio si se uso por error
    nombre = nombre[0].upper() + nombre[1:] #primera letra siempre en mayúscula
    print()#linia en blanca
    return nombre

def validarNumTelf():
    correcto = False
    while not correcto:
        telefono = input('Teléfono del cliente: ').strip()

        if telefono.isdigit() and len(telefono) == 9:
            print("Número de teléfono correcto.")
            return telefono
        else:
            print("Número de teléfono incorrecto.\n")
        print()#linia en blanco

def inserta_telefono(fichero, persona, telefono):
    # persona: string del nombre que pondremos en el menú
    # telefono: string del teléfono que también pondremos en el menú
    try:
        with open(fichero, "a") as archivo:
            archivo.write(f"{persona},{telefono}\n")
        print(f"\nCliente {persona} con el número {telefono} añadido correctamente\n")
    except Exception as e:
        print(f"Error al introducir el teléfono: {e}\n")

def elimina_telefono(fichero, persona):
    eliminado = False
    try:
        with open(fichero, "r") as archivo:
            lineas = archivo.readlines()
        with open(fichero, "w") as archivo:
            for linea in lineas:
                nombre, telefono = linea.strip().split(",")
                if nombre.lower() != persona.lower():
                    archivo.write(linea)
                else:
                    eliminado = True
        if eliminado:
            print(f"Cliente {persona} eliminado correctamente.\n")
        else:
            print(f"No se encontró ningún cliente con el nombre '{persona}'.\n")
    except FileNotFoundError:
        print("Error: El archivo agenda.txt no existe.\n")
    except Exception as e:
        print(f"Error al eliminar teléfono: {e}\n")

def obten_telefono(fichero, persona):
    encontrado = False
    try:
        with open(fichero, "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(",")
                if nombre.lower() == persona.lower():
                    print(f"Teléfono de {nombre}: {telefono}\n")
                    encontrado = True
                    break
        if not encontrado:
            print(f"No existe ningún cliente con el nombre '{persona}'.\n")
    except FileNotFoundError:
        print("Error: El archivo agenda.txt no existe.\n")
    except Exception as e:
        print(f"Error al obtener teléfono: {e}\n")

def salir_Menu():
    print('Saliendo del menú')
    return True

def menu():
    salir = False
    while not salir:
        print('______ MENÚ ______\n')
        print("1. Obtener un teléfono")
        print("2. Insertar un teléfono")
        print("3. Eliminar un teléfono")
        print("4. Salir\n")

        op = (input('Seleccione una opción: '))

        if op == "1":
            persona = introducirNombre()
            obten_telefono(fichero, persona)
        elif op == "2":
            persona = introducirNombre()
            telefono = validarNumTelf()
            inserta_telefono(fichero, persona, telefono)
        elif op == "3":
            persona = introducirNombre()
            elimina_telefono(fichero, persona)
        elif op == "4":
            salir = salir_Menu()
        else:
            print()
            print('Debe seleccionar una opción de 1 a 4.\n')
            print()

# PROGRAMA
menu()