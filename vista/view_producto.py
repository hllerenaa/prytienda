from controlador.ctr_producto import Controlador
from controlador.ctr_linea import Controlador as ControladorLinea
from controlador.ctr_marca import Controlador as ControladorMarca

class Vista:

    def __init__(self):
        self.controlador = Controlador()
        self.ctrl_linea = ControladorLinea()
        self.ctrl_marca = ControladorMarca()

    def iniciar(self):
        while True:
            print("\n----- SISTEMA DE PRODUCTOS -----")
            print("1. Agregar producto")
            print("2. Listar productos")
            print("3. Editar producto")
            print("4. Eliminar producto")
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

    def mostrar(self, productos):
        if len(productos) == 0:
            print("\nNo hay productos guardados.")
            return
        # build maps for names
        lineas = {l.id: l.nombre for l in self.ctrl_linea.listar()}
        marcas = {m.id: m.nombre for m in self.ctrl_marca.listar()}
        print("\n----- PRODUCTOS -----")
        for d in productos:
            nombre_linea = lineas.get(d.linea_id, "-")
            nombre_marca = marcas.get(d.marca_id, "-")
            print(f"id: {d.id} - Nombre: {d.nombre} - Linea: {d.linea_id} ({nombre_linea}) - Marca: {d.marca_id} ({nombre_marca})")

    def agregar(self):
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("Nombre no puede estar vacio.")
            return

        lineas = self.ctrl_linea.listar()
        if len(lineas) == 0:
            print("No hay lineas. Crea una linea antes de agregar productos.")
            return
        print("\nLineas disponibles:")
        for l in lineas:
            print(f"id: {l.id} - {l.nombre}")
        linea_id = input("Id de la linea: ").strip()
        if not linea_id.isdigit() or int(linea_id) not in [l.id for l in lineas]:
            print("Linea invalida.")
            return

        marcas = self.ctrl_marca.listar()
        if len(marcas) == 0:
            print("No hay marcas. Crea una marca antes de agregar productos.")
            return
        print("\nMarcas disponibles:")
        for m in marcas:
            print(f"id: {m.id} - {m.nombre}")
        marca_id = input("Id de la marca: ").strip()
        if not marca_id.isdigit() or int(marca_id) not in [m.id for m in marcas]:
            print("Marca invalida.")
            return

        try:
            self.controlador.agregar(nombre, int(linea_id), int(marca_id))
            print("\nProducto agregado.")
        except Exception as ex:
            print(f"\nNo se pudo agregar el producto: {ex}")

    def listar(self):
        productos = self.controlador.listar()
        self.mostrar(productos)

    def editar(self):
        print("\nPara editar un registro debes ingresar un ID.")
        productos = self.controlador.listar()
        self.mostrar(productos)

        id = input("\nId del producto a editar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma editar el producto con id {id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operacion cancelada.")
            return

        nuevo_nombre = input("Nombre: ").strip()
        if nuevo_nombre == "":
            print("Nombre no puede estar vacio.")
            return

        lineas = self.ctrl_linea.listar()
        print("\nLineas disponibles:")
        for l in lineas:
            print(f"id: {l.id} - {l.nombre}")
        linea_id = input("Id de la linea: ").strip()
        if not linea_id.isdigit() or int(linea_id) not in [l.id for l in lineas]:
            print("Linea invalida.")
            return

        marcas = self.ctrl_marca.listar()
        print("\nMarcas disponibles:")
        for m in marcas:
            print(f"id: {m.id} - {m.nombre}")
        marca_id = input("Id de la marca: ").strip()
        if not marca_id.isdigit() or int(marca_id) not in [m.id for m in marcas]:
            print("Marca invalida.")
            return

        try:
            self.controlador.editar(id, nuevo_nombre, int(linea_id), int(marca_id))
            print("\nProducto editado.")
        except Exception as ex:
            print(f"\nNo se pudo editar el producto: {ex}")

    def eliminar(self):
        print("\nPara eliminar un registro debes ingresar un ID.")
        productos = self.controlador.listar()
        self.mostrar(productos)

        id = input("\nId del producto a eliminar: ")
        if not id.isdigit():
            print("El id debe ser un numero.")
            return

        confirm = input(f"Confirma eliminar el producto con id {id}? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operacion cancelada.")
            return

        try:
            self.controlador.eliminar(id)
            print("\nProducto eliminado.")
        except Exception as ex:
            print(f"\nNo se pudo eliminar el producto: {ex}")
