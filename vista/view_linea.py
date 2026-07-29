from controlador.ctr_linea import Controlador

class Vista:

    def __init__(self):
        # La Vista usa un Controlador para guardar y leer los datos.
        self.controlador = Controlador()

    def iniciar(self):
        # Este es el menu del catalogo: se repite hasta que el usuario elige regresar.
        while True:
            print("\n----- SISTEMA DE LINEAS -----")
            print("1. Agregar linea")
            print("2. Listar lineas")
            print("3. Editar linea")
            print("4. Eliminar linea")
            print("5. Regresar")
            opcion = input("Elige una opcion: ")

            if opcion == "1":
                self.agregar()
            elif opcion == "2":
                self.listar()
            elif opcion == "3":
                self.editar()
            elif opcion == "4":
                self.eliminar()
            elif opcion == "5":
                # Regresa al menu principal (solo rompe ESTE menu).
                print("\nRegresando al menu principal...")
                break
            else:
                print("\nOpcion no valida. Elige del 1 al 5.")


    def mostrar(self, lineas):
        # Muestra la lista numerada (1, 2, 3...).
        # OJO: el "numero" de la lista es solo la posicion en pantalla para
        # elegir; el "id" es el identificador real y unico de cada linea
        # (lo genero el Modelo de forma automatica) y no cambia aunque borres.
        if len(lineas) == 0:
            print("\nNo hay lineas guardadas.")
            return
        print("\n----- LINEAS -----")
        numero = 1
        for d in lineas:
            print(f"id: {d.id} - Nombre: {d.nombre}")
            numero = numero + 1

    def agregar(self):
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("Nombre no puede estar vacio.")
            return

        # try / except: si al guardar algo falla (por ejemplo, no se puede
        # escribir el archivo), NO se cae el programa. Mostramos el error y
        # el menu sigue funcionando.
        try:
            self.controlador.agregar(nombre)
            print("\nLinea agregada.")
        except Exception as ex:
            print(f"\nNo se pudo agregar la linea: {ex} estoy aqui")

    def listar(self):
        lineas = self.controlador.listar()
        self.mostrar(lineas)

    def editar(self):
        print("\nPara editar un registro debes ingresar un ID.")
        lineas = self.controlador.listar()
        self.mostrar(lineas)

        id = input("\nId de la linea a editar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma editar la linea con id {id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operacion cancelada.")
            return

        print(f"Ingrese nuevo nombre:")
        nuevo_nombre = input("Nombre: ").strip()
        if nuevo_nombre == "":
            print("Nombre no puede estar vacio.")
            return

        try:
            self.controlador.editar(id, nuevo_nombre)
            print("\nLinea editada.")
        except Exception as ex:
            print(f"\nNo se pudo editar la linea: {ex}")


    def eliminar(self):
        print("\nPara eliminar un registro debes ingresar un ID.")
        lineas = self.controlador.listar()
        self.mostrar(lineas)

        id = input("\nId de la linea a eliminar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma eliminar la linea con id {id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operacion cancelada.")
            return

        # try / except: si el id NO existe, el controlador lanza un error
        # y aqui lo atrapamos para mostrar el mensaje sin caernos.
        try:
            self.controlador.eliminar(id)
            print("\nLinea eliminada.")
        except Exception as ex:
            print(f"\nNo se pudo eliminar la linea: {ex}")