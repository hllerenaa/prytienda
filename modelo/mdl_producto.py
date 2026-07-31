class Producto:

    def __init__(self, nombre, linea_id, marca_id, id):
        self._id = id
        self._nombre = nombre
        self._linea_id = linea_id
        self._marca_id = marca_id

    @staticmethod
    def siguiente_id(productos):
        mayor = 0
        for p in productos:
            if p.id > mayor:
                mayor = p.id
        return mayor + 1

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def linea_id(self):
        return self._linea_id

    @property
    def marca_id(self):
        return self._marca_id
