import unittest
from Grille import *
from copy import deepcopy

class TestGrille(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.getGrilleSimple = getGrilleSimple()
        self.grillePossible = getGrillePossible()

    def test_removeValuesFromList(self):
        liste1 = [1, 4, 5, 7, 8]
        liste2 = [2, 5]

        listeSimplifiee = removeValuesFromList(liste1, liste2)
        listeSimplifiee.sort()
        self.assertEqual(listeSimplifiee, [1,4,7,8])

    def test_getObviousAnswerOrFalse(self):
        grille = Grille()
        grille.setGrille(self.getGrilleSimple)
        ObviousAnswerOrFalse = grille.getObviousAnswerOrFalse(grille.grilleData, 4,4)
        self.assertEqual(ObviousAnswerOrFalse, 8)


    def test_solveIteration(self):
        """
        si cette fonction marche, les fonctions ValuesInLine, valuesInColumn et valuesInBlock devraient foncitonner aussi
        """
        grille = Grille()
        grille.setGrille(self.getGrilleSimple)
        grille.solution = deepcopy(grille.grilleData)
        grille.solveIteration(grille.grilleData)
        self.assertEqual(grille.solution, [
                [-1,-1,-1,-1,4,-1,-1,-1,-1],
                [-1,-1,-1,-1,5,-1,-1,-1,-1],
                [-1,-1,-1,-1,6,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [1,2,3,-1,8,-1,-1,-1,-1],
                [-1,-1,-1,7,-1,9,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        )

    def test_solveIncomplet(self):
        grille = Grille()
        grille.setGrille(self.grillePossible)
        grille.solve()
        self.assertEqual(grille.solution, [
                [2,9,4,7,-1,3,1,8,6,],
                [1,5,6,2,8,9,3,4,7,],
                [3,8,7,-1,6,5,-1,9,2,],
                [5,7,1,3,9,2,4,6,8,],
                [4,2,3,6,1,8,7,5,9,],
                [8,6,9,5,4,7,2,3,1,],
                [9,4,2,8,-1,1,5,7,3,],
                [6,1,8,-1,-1,4,9,2,6,],
                [7,3,5,9,2,6,8,1,4,]]
        )


    

if __name__ == "__main__":
    unittest.main()