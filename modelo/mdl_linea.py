class Linea:

    def __init__(self, nombre, id):
        self._id = id
        self._nombre = nombre

    @staticmethod
    def siguiente_id(lineas):
        """
        Devuelve el id que le toca a una linea NUEVA.

        Regla (muy sencilla): es el id mas alto que ya existe + 1.
        Si todavia no hay ninguna linea, empezamos en 1.

        Ejemplo: si ya existen los ids 1, 2 y 5 -> devuelve 6.

        Es @staticmethod porque NO necesita una linea concreta (no usa 'self'):
        solo mira la lista completa. Por eso se llama con Linea.siguiente_id(...).
        """
        mayor = 0
        for linea in lineas:
            if linea.id > mayor:
                mayor = linea.id
        return mayor + 1

    @staticmethod
    def encriptar_id(id):
        # Ejemplo simple de encriptación (puede ser reemplazada por una lógica más compleja)
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