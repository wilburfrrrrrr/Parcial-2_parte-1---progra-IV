from model.productoControl import ProductoControl
from model.pedido import Pedido
import unittest

class TestPedido(unittest.TestCase):
    def test_agregar_producto(self):
        pedido = Pedido()
        producto = ProductoControl("123", "Fertilizante A", "Quincenal", 50.0)
        pedido.agregar_producto(producto)
        self.assertEqual(len(pedido.productos), 1)
        self.assertEqual(pedido.productos[0], producto)

    def test_calcular_total(self):
        pedido = Pedido()
        producto1 = ProductoControl("123", "Fertilizante A", "Quincenal", 50.0)
        producto2 = ProductoControl("456", "Fertilizante B", "Mensual", 30.0)
        pedido.agregar_producto(producto1)
        pedido.agregar_producto(producto2)
        total = pedido.calcular_total()
        self.assertEqual(total, 80.0)
        
if __name__ == "__main__":
    unittest.main()