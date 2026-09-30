from Grille import *
import math

GrillePossible = getGrilleSimple()

grille = Grille()
grille.setGrille(getGrillePossible())
grille.printGrille()
grille.solve()
grille.printSolution()# 