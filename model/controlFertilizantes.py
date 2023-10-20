from .productoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(ica, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

        