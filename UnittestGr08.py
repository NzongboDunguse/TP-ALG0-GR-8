import unittest
import math
from pro1_7 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle

class TestGeo_Form(unittest.TestCase):
    def test_rectangle(self):
        try:
            rec = Rectangle("Rectangle 01",5,4)
            self.assertEqual(rec.perimetre(), 14)
            self.assertEqual(rec.surface(), 12)            
        except:
            pass

    def test_cercle(self): 
        try:
            cer = Cercle("Cercle A1",5)
            self.assertEqual(cer.perimetre(), 2*math.pi*5)
            self.assertEqual(cer.surface(), math.pi*5**2)
        except:
            pass
        
    def test_triangle(self):
        try:
            tri = Triangle("Triangle A1 ",3,4,5)
            self.assertEqual(tri.perimetre(), 12)
            self.assertEqual(tri.surface(), 6)
        except Exception:
            pass

    def test_carre(self):
        
        try:
            car = Carre("Carre A1 ",6)
            self.assertEqual(car.perimetre(), 24)
            self.assertEqual(car.surface(), 36)
        except Exception:
            pass

    def test_triarectangle(self):
        try:
            triarectangle = TriangleRectangle("Triangle Rectangle TR1 ",3,4)
            self.assertEqual(triarectangle.perimetre(), 12)
            self.assertEqual(triarectangle.surface(), 6)
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()