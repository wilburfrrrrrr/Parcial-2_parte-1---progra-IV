class ProductoControl:
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor):
        if valor < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.ica = ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor

        