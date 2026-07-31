import os, sys

from modelo.mdl_marca import Marca


class Controlador:

    def __init__(self):
        # Preparamos la ruta del archivo: media/marcas.txt
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)
        self.archivo = os.path.join(carpeta, "marcas.txt")

    def listar(self):
        marcas = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for l in archivo:
                    l = l.strip()
                    if l == "":
                        continue
                    id, nombre = l.split(",", 1)
                    marca = Marca(nombre, int(id))
                    marcas.append(marca)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')
        return marcas

    def guardar(self, marcas):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for d in marcas:
                archivo.write(f"{d.id},{d.nombre}\n")

    def agregar(self, nombre):
        try:
            marcas = self.listar()
            nuevo_id = Marca.siguiente_id(marcas)
            marcas.append(Marca(nombre, nuevo_id))
            self.guardar(marcas)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')

    def editar(self, id, nombre_actual):
        marcas = self.listar()
        id = int(id)
        for i in range(len(marcas)):
            if marcas[i].id == id:
                marcas[i] = Marca(nombre_actual, id)
                self.guardar(marcas)
                return

    def eliminar(self, id):
        marcas = self.listar()
        id = int(id)
        for i in range(len(marcas)):
            if marcas[i].id == id:
                marcas.pop(i)
                self.guardar(marcas)
                return
        raise ValueError(f"No existe una marca con id {id}")
