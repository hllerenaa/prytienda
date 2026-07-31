from controlador.ctr_marca import Controlador

class Vista:

    def __init__(self):
        self.controlador = Controlador()

    def iniciar(self):
        while True:
            print("\n----- SISTEMA DE MARCAS -----")
            print("1. Agregar marca")
            print("2. Listar marcas")
            print("3. Editar marca")
            print("4. Eliminar marca")
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
                print("\nRegresando al menu principal...")
                break
            else:
                print("\nOpcion no valida. Elige del 1 al 5.")

    def mostrar(self, marcas):
        if len(marcas) == 0:
            print("\nNo hay marcas guardadas.")
            return
        print("\n----- MARCAS -----")
        for d in marcas:
            print(f"id: {d.id} - Nombre: {d.nombre}")

    def agregar(self):
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("Nombre no puede estar vacio.")
            return
        try:
            self.controlador.agregar(nombre)
            print("\nMarca agregada.")
        except Exception as ex:
            print(f"\nNo se pudo agregar la marca: {ex}")

    def listar(self):
        marcas = self.controlador.listar()
        self.mostrar(marcas)

    def editar(self):
        print("\nPara editar un registro debes ingresar un ID.")
        marcas = self.controlador.listar()
        self.mostrar(marcas)

        id = input("\nId de la marca a editar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma editar la marca con id {id}? (s/n): ").strip().lower()
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
            print("\nMarca editada.")
        except Exception as ex:
            print(f"\nNo se pudo editar la marca: {ex}")

    def eliminar(self):
        print("\nPara eliminar un registro debes ingresar un ID.")
        marcas = self.controlador.listar()
        self.mostrar(marcas)

        id = input("\nId de la marca a eliminar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma eliminar la marca con id {id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operacion cancelada.")
            return

        try:
            self.controlador.eliminar(id)
            print("\nMarca eliminada.")
        except Exception as ex:
            print(f"\nNo se pudo eliminar la marca: {ex}")
