class Marca:

    def __init__(self, nombre, id):
        self._id = id
        self._nombre = nombre

    @staticmethod
    def siguiente_id(marcas):
        """
        Devuelve el id que le toca a una marca NUEVA.
        """
        mayor = 0
        for marca in marcas:
            if marca.id > mayor:
                mayor = marca.id
        return mayor + 1

    @staticmethod
    def encriptar_id(id):
        return id * 2 + 1

    @staticmethod
    def decriptar_id(id):
        return id * 2

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
