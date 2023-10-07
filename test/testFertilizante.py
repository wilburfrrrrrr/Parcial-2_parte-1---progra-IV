import unittest
from model.controlFertilizantes import ControlFertilizantes

class TestControlFertilizantes(unittest.TestCase):
    def test_creacion_control_fertilizantes(self):
        control_fertilizantes = ControlFertilizantes("456", "Fertilizante B", "Mensual", 30.0, "2023-10-10")
        self.assertEqual(control_fertilizantes.ica, "456")
        self.assertEqual(control_fertilizantes.nombre, "Fertilizante B")
        self.assertEqual(control_fertilizantes.frecuencia_aplicacion, "Mensual")
        self.assertEqual(control_fertilizantes.valor, 30.0)
        self.assertEqual(control_fertilizantes.fecha_ultima_aplicacion, "2023-10-10")

if __name__ == "__main__":
    unittest.main() 