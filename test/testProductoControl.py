test
from model.productoControl import ProductoControl


class TestProductoControl(unittest.TestCase):
    def test_creacion_producto_control(self):
        producto_control = ProductoControl("789", "Producto C", "Anual", 10.0)
        self.assertEqual(producto_control.ica, "789")
        self.assertEqual(producto_control.nombre, "Producto C")
        self.assertEqual(producto_control.frecuencia_aplicacion, "Anual")
        self.assertEqual(producto_control.valor, 10.0)
        
    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            producto_control = ProductoControl("789", "Producto C", "Anual", -10.0)
    
    def test_ica_vacio(self):
        with self.assertRaises(ValueError):
            producto_control = ProductoControl("", "Producto C", "Anual", 10.0)
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            producto_control = ProductoControl("789", "", "Anual", 10.0)
            
    def test_frecuencia_vacio(self):
        with self.assertRaises(ValueError):
            producto_control = ProductoControl("789", "Producto C", "", 10.0)
    
    def test_valor_vacio(self):
        with self.assertRaises(ValueError):
            producto_control = ProductoControl("789", "Producto C", "Anual", "")


if __name__ == "__main__":
    unittest.main()