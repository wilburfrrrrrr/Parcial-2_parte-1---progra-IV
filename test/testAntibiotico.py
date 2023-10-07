import unittest
from model.antibiotico import Antibiotico

class TestAntibiotico(unittest.TestCase):
    def test_creacion_antibiotico(self):
        antibiotico = Antibiotico("Antibiótico X", 500, "Bovino", 25.0)
        self.assertEqual(antibiotico.nombre, "Antibiótico X")
        self.assertEqual(antibiotico.dosis, 500)
        self.assertEqual(antibiotico.tipo_animal, "Bovino")
        self.assertEqual(antibiotico.valor, 25.0)

if __name__ == "__main__":
    unittest.main()