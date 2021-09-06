import Libreria2 as lc
import unittest
class TestCplxoperations(unittest.TestCase):
    def test_Suma(self):
        self.assertEqual(lc.sumvectores([(1,0),(2,0)],[(3,0),(7,0)]), [(1, 0, 3, 0), (2, 0, 7, 0)])
    def test_Resta(self):
        self.assertEqual(lc.inverso([(-1,0),(2,0)]), [-(-1, 0),-(2, 0)])
        """
    def test_Multiplicacion(self):
        self.assertEqual(lc.multescalar([(1,0),(2,0)],3), [3(1, 0),3(2, 0)])
"""
if __name__ == "__main__":
    unittest.main()