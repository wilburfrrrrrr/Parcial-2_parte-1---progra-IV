import datetime

class Pedido:
    def __init__(self):
        self.fecha = datetime.date.today()
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = sum(producto.valor for producto in self.productos)
        return total