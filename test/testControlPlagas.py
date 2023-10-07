import unittest
from model.controlPlagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    def test_creacion_control_plagas(self):
        control_plagas = ControlPlagas("123", "Plaguicida A", "Quincenal", 50.0, 7)
        self.assertEqual(control_plagas.ica, "123")
        self.assertEqual(control_plagas.nombre, "Plaguicida A")
        self.assertEqual(control_plagas.frecuencia_aplicacion, "Quincenal")
        self.assertEqual(control_plagas.valor, 50.0)
        self.assertEqual(control_plagas.periodo_carencia, 7)

if __name__ == "__main__":
    unittest.main()
