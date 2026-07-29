import os, sys
from asyncio import exceptions

from modelo.mdl_linea import Linea


class Controlador:

    def __init__(self):
        # Preparamos la ruta del archivo: media/lineas.txt
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)   # crea la carpeta si no existe
        self.archivo = os.path.join(carpeta, "lineas.txt")

    def listar(self):
        # Lee el archivo y devuelve una lista de objetos Linea.
        lineas = []

        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for l in archivo:
                    l = l.strip()
                    if l == "":
                        continue
                    # Cada fila trae 2 datos: id y nombre.
                    id, nombre = l.split(",", 1)
                    # Pasamos el id para CONSERVAR el que ya tenia guardado.
                    # int(id) porque del archivo todo se lee como texto,
                    # y siguiente_id() necesita compararlo como numero.
                    linea = Linea(nombre, int(id))
                    lineas.append(linea)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')
        return lineas

    def guardar(self, lineas):
        # Escribe TODA la lista en el archivo (borra lo viejo y pone lo nuevo).
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for d in lineas:
                # Guardamos tambien el id al principio de cada fila.
                archivo.write(f"{d.id},{d.nombre}\n")

    def agregar(self, nombre):
        try:
            lineas = self.listar()
            # Pedimos el id nuevo al metodo del Modelo: el mas alto + 1.
            nuevo_id = Linea.siguiente_id(lineas)
            lineas.append(Linea(nombre, nuevo_id))
            self.guardar(lineas)
        except Exception as ex:
            print(f'Error on line {sys.exc_info()[-1].tb_lineno}, {ex}')

    def editar(self, id, nombre_actual):
        lineas = self.listar()
        id = int(id)
        for i in range(len(lineas)):
            if lineas[i].id == id:
                lineas[i] = Linea(nombre_actual, id)
                self.guardar(lineas)
                return

    def eliminar(self, id):
        lineas = self.listar()
        id = int(id)
        for i in range(len(lineas)):
            if lineas[i].id == id:
                lineas.pop(i)          # la encontramos: la quitamos
                self.guardar(lineas)
                return
        # Si no aparece ningun id igual, lanzamos el error.
        raise ValueError(f"No existe una linea con id {id}")

        # lineas_temporal = [l for l in lineas if l.id != int(id)]
        # self.guardar(lineas)

