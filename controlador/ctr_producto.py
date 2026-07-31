import os, sys

from modelo.mdl_producto import Producto


class Controlador:

    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)
        self.archivo = os.path.join(carpeta, "productos.txt")

    def listar(self):
        productos = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for l in archivo:
                    l = l.strip()
                    if l == "":
                        continue
                    # id,nombre,linea_id,marca_id
                    partes = l.split(',', 3)
                    if len(partes) < 4:
                        continue
                    id, nombre, linea_id, marca_id = partes
                    producto = Producto(nombre, int(linea_id), int(marca_id), int(id))
                    productos.append(producto)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')
        return productos

    def guardar(self, productos):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for d in productos:
                archivo.write(f"{d.id},{d.nombre},{d.linea_id},{d.marca_id}\n")

    def agregar(self, nombre, linea_id, marca_id):
        try:
            productos = self.listar()
            nuevo_id = Producto.siguiente_id(productos)
            productos.append(Producto(nombre, int(linea_id), int(marca_id), nuevo_id))
            self.guardar(productos)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')

    def editar(self, id, nombre_actual, linea_id, marca_id):
        productos = self.listar()
        id = int(id)
        for i in range(len(productos)):
            if productos[i].id == id:
                productos[i] = Producto(nombre_actual, int(linea_id), int(marca_id), id)
                self.guardar(productos)
                return

    def eliminar(self, id):
        productos = self.listar()
        id = int(id)
        for i in range(len(productos)):
            if productos[i].id == id:
                productos.pop(i)
                self.guardar(productos)
                return
        raise ValueError(f"No existe un producto con id {id}")
