# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:16:32 2023
@author: GROUPE8
NZONGBO DUNGUSE
MVALA MASASU
"""
from pro1_8 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig, tout_perimetre, tout_superficie, decris_toi  
if __name__ == '__main__':
    try:
        rectangle = Rectangle("Rectangle A1", 14, 7)
        cercle = Cercle("Cercle A2", 14)
        triangle = Triangle("Triangle A3", 9, 6, 7)
        carre = Carre("Carré A4", 6)
        t_rectangle = TriangleRectangle("Triangle Rectangle A5", 5, 7)
        
        print()
        print("Pour le polymorphisme\n")
        decris_toi(rectangle)
        print()
        decris_toi(cercle)
        print()
        decris_toi(triangle)
        print()
        decris_toi(carre)
        print()
        decris_toi(t_rectangle)
        print()
        
    except Exception:
        print("Parametres non pris en charge.")
