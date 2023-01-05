# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:16:32 2023
@author: GROUPE8
NZONGBO DUNGUSE
MVALA MASASU
"""
from abc import ABCMeta, abstractmethod
from math import pi, sqrt
class Geo_Form(metaclass = ABCMeta):
    @abstractmethod
    def perimetre():
        pass

    @abstractmethod
    def surface():
        pass
    
    def decris_toi(self):
        print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(self.nomF, self.perimetre(), self.surface()))
        
class Rectangle(Geo_Form):
    try:
        def __init__(self,nomF, longueur, largeur):
            self.nomF = nomF
            self.longueur = longueur
            self.largeur = largeur
        def perimetre(self):
            return 2*self.longueur + 2*self.largeur
        
        def surface(self):
            return self.longueur*self.largeur
    except:
        print("Parametres non pris en charge")

class Cercle(Geo_Form):  
    try:
        def __init__(self, nomF, rayon):
            self.nomF = nomF
            self.rayon = rayon
        def perimetre(self):
            return 2*pi*self.rayon
        def surface(self):
            return  pi*(self.rayon**2)
    except:
        print("Parametres non pris en charge")

class Triangle(Geo_Form):
    try:
        def __init__(self,nomF, coteA,coteB,coteC):
            self.nomF = nomF
            self.coteB = coteB
            self.coteA = coteA
            self.coteC = coteC
        def perimetre(self):
            return self.coteB + self.coteA + self.coteC

        def surface(self):
            p = self.perimetre()/2
            aire = sqrt(p*(p - self.coteA)*(p - self.coteB)*(p - self.coteC))
            aire = aire.real
            return aire
    except:
        print("Parametres non pris en charge")
class Carre(Rectangle):
    try:
        def __init__(self,nomF, cote):
            Rectangle.__init__(self, nomF, cote, cote)
    except:
        print("Parametres non pris en charge ")

class TriangleRectangle(Triangle):
    try:
        def __init__(self,nomF, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, nomF, base, hauteur, hyp)
    except:
        print("Parametres non pris en charge ")

class GeoFig():  
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def decris_toi(self):
            for g in self.gGeo_rep:
                print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(g.nomF, g.perimetre(), g.surface()))
    except:
        print("Parametres non pris en charge")
