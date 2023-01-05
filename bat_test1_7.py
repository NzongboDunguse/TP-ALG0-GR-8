# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:16:32 2023
@author: GROUPE8
NZONGBO DUNGUSE
MVALA MASASU
"""
from pro1_7 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig  
if __name__ == '__main__':
    print("Depuis les classes seules :")
    print()
    try:
        rectangle = Rectangle("Rectangle A1", 14, 7)
        cercle = Cercle("Cercle A2", 14)
        triangle = Triangle("Triangle A3", 9, 6, 7)
        carre = Carre("Carré A4", 6)
        t_rectangle = TriangleRectangle("Triangle Rectangle A5", 5, 7)
        
        rectangle.decris_toi()
        print()
        cercle.decris_toi()
        print()
        triangle.decris_toi()
        print()
        carre.decris_toi()
        print()
        t_rectangle.decris_toi()
        print()
    except Exception:
        print("Parametres non pris en charge.")
    
    print()
    print()
    print("Depuis la classe Globale : ")
    print()
    figA = GeoFig() 
    figB = GeoFig() 
    figC = GeoFig()
    figD = GeoFig()
    figE = GeoFig()
    
    figA.add(Rectangle("Rectangle B1", 12, 5))
    figB.add(Cercle("Cercle B2", 5))
    figC.add(Triangle("Triangle B3", 9, 6, 7))
    figD.add(Carre("Carré B4", 10))
    figE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
    
    figA.decris_toi()
    figB.decris_toi()
    figC.decris_toi()
    figD.decris_toi()
    figE.decris_toi()
    
    try:
        pass

    except Exception:
        print("Parametres non pris en charge.")        
