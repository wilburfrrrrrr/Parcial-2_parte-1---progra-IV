from .productoControl import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        if periodo_carencia < 0:
            raise ValueError("El periodo de carencia no puede ser negativo.")
        super().__init__(ica, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia
        