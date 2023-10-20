from model.cliente import Cliente
from model.pedido import Pedido
import unittest

class TestCliente(unittest.TestCase):        
    def test_creacion_cliente(self):
        cliente = Cliente("Juan Pérez", "1234567890")
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.cedula, "1234567890")

    def test_agregar_pedido(self):
        cliente = Cliente("Juan Pérez", "1234567890")
        pedido = Pedido()
        cliente.agregar_pedido(pedido)
        self.assertEqual(len(cliente.pedidos), 1)
        self.assertEqual(cliente.pedidos[0], pedido)

if __name__ == "__main__":
    unittest.main()