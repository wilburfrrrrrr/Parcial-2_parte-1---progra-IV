import unittest
from model.productoControl import ProductoControl

class TestProductoControl(unittest.TestCase):
    def test_creacion_producto_control(self):
        producto_control = ProductoControl("789", "Producto C", "Anual", 10.0)
        self.assertEqual(producto_control.ica, "789")
        self.assertEqual(producto_control.nombre, "Producto C")
        self.assertEqual(producto_control.frecuencia_aplicacion, "Anual")
        self.assertEqual(producto_control.valor, 10.0)

if __name__ == "__main__":
    unittest.main()
