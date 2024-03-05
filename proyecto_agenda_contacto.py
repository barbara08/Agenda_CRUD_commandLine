import os

CARPETA = "contactos/"
EXTENSION = ".txt"

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()
    # mostrar menú de opciones
    mostrar_menu()
    # Preguntar al uasuario
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opción: \r\n")
        opcion = int(opcion)
        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            #print("Agregar Contacto: ")
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            #print("Editar Contacto: ")
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            #print("Ver Contactos: ")
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            #print("Buscar Contacto: ")
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            #print("Eliminar Contacto: ")
            preguntar = False
        elif opcion == 6:
            #print("Salir: ")
            #preguntar = False  # No volver a preguntar
            break               # Salir automáticamente con break
        else:
            print("Opción no válida")

def crear_directorio():
    # Comprobar si exite
    if not os.path.isdir(CARPETA):   # Buscará un directorio
    #if not os.path.exists(CARPETA): # Buscará cualquiere cosa (fichero, carpeta, etc)
        # Si no existe lo crearlo
        os.makedirs(CARPETA)
    # No es necesario else, solo es para mostrar que ya existe la carpeta
    else:
        print("La carpeta ya existe")

def mostrar_menu():
    print("Elige una opción: ")
    print("1) Agregar Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")
    print("6) Salir")

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def agregar_contacto():
    # Pedir los datos al usuario
    print("Añade los datos del contacto: ")
    nombre_contacto = input("Nombre del contacto: \r\n")
    # Revisar si el archivo existe antes de crearlo
    # Anotar la ruta completa
    existe = existe_contacto(nombre_contacto)
    # Si no exite lo crea
    if not existe:
            # Crea la carpeta => contactos/ => Guarda => contactos/juan.txt
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            # Pedir al usurio el resto de los campos
            telefono_contacto = input("Teléfono de contacto: \r\n")
            categoria_contacto = input("Categoría del contacto: \r\n")

            # Instanciar la clase 
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo los datos
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

            # Mostrar mensaje de éxito
            print(("Contacto creado correctamente"))
    
    else: 
        print("Contacto ya existe")

    # Reiniciar la app() para que vuelva a pedir los datos
    app()

def editar_contacto():
    # Solicitar el nombre que quiere editar
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input("Nombre del contacto a editar: \r\n")

    # Revisar si el nombre existe antes de editarlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        # Puede editarlo
        print("Puede editarlo")
        # Abrir la carpeta
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            # Solictar resto de campos a editar
            nombre_contacto = input("Agrega el nuevo nombre de contacto: \r\n")
            telefono_contacto = input("Agrega el nuevo teléfono de contacto: \r\n")
            categoria_contacto = input(" Agrega la nueva Categoría del contacto: \r\n")

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Teléfono: " + contacto.telefono + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

            # Renombrar el archivo (nombre archivo anterior, nombre del nuevo archivo)
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar mensaje de éxito
            print(("Contacto editado correctamente"))
    else:
        # No lo puede editar porque no existe
        print("Contacto no existe")
        # Reinicia app() para que vuelva a ejecutarse
        app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    print("archivos", archivos)
    
    # Busca en la carpeta contactos/ todos los archivos con extensión txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    print("archivos_txt", archivos_txt)

    # Recorremos todos los archivos.txt y lo guardamos en archivo
    for archivo in archivos_txt:
        
        # Abrimos todos los archivos (contactos)
        with open(CARPETA + archivo) as contacto:
            
            # Recorremos todos los contactos
            for linea in contacto:
                # Imprime el contenido de cada contacto (quitándole los espacios rstrip())
                print(linea.rstrip())
            # Fuera del for anotamos para imprimir separador entre contactos
            print("\r\n")
    # Reiniciar la app()
    app()

# Con esta función no hay excepción
# Por lo que si un contacto no se encuntra mostrar información de error
def buscar_contacto1():
    nombre_contacto = input("Introduce el nombre para buscar: \r\n")

    with open(CARPETA + nombre_contacto + EXTENSION) as contacto:
        #print(contacto)
        print("Información del Contacto: \r\n")
        for linea in contacto:
            print(linea.rstrip())
        print("\r\n")

# Con esta función miramos excepción
# En caso de que no encuentre un contacto no salte el error
def buscar_contacto():
    nombre_contacto = input("Introduce el nombre para buscar: \r\n")

    try:
        with open(CARPETA + nombre_contacto + EXTENSION) as contacto:
            #print(contacto)
            print("Información del Contacto: \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")
    except IOError:
        print("Contacto no encontrado")
        print(IOError)
    
    # Reiniciar la app()
    app()

def eliminar_contacto():
    nombre_contacto = input("Introduce el nombre que desee eliminar: \r\n")

    try:
        os.remove(CARPETA + nombre_contacto + EXTENSION)
    except:
        print("No existe ese contacto")

    # Reinicar la app()
    app()

app()
