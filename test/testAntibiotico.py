import unittest
from model.antibiotico import Antibiotico


class TestAntibiotico(unittest.TestCase):
    
    def test_creacion_antibiotico(self):
        antibiotico = Antibiotico("Antibiótico X", 500, "Bovino", 25.0)
        self.assertEqual(antibiotico.nombre, "Antibiótico X")
        self.assertEqual(antibiotico.dosis, 500)
        self.assertEqual(antibiotico.tipo_animal, "Bovino")
        self.assertEqual(antibiotico.valor, 25.0)
        
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            antibiotico = Antibiotico("", 500, "Bovino", 25.0)
            
    def test_dosis_menor_400(self):
        with self.assertRaises(ValueError):
            antibiotico = Antibiotico("Antibiótico X", 300, "Bovino", 25.0)
            
    def test_dosis_mayor_600(self):
        with self.assertRaises(ValueError):
            antibiotico = Antibiotico("Antibiótico X", 700, "Bovino", 25.0)
    
    def test_tipo_animal_invalido(self):
        with self.assertRaises(ValueError):
            antibiotico = Antibiotico("Antibiótico X", 500, "Perro", 25.0)
    
    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            antibiotico = Antibiotico("Antibiótico X", 500, "Bovino", -25.0)
        
if __name__ == "__main__":
    unittest.main()