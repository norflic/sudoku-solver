import math
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Position:
    x: int
    y: int
    
def getEmptyGrille():
    return([[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1]])

def getGrilleSimple():
    return([[-1,-1,-1,-1,4,-1,-1,-1,-1],[-1,-1,-1,-1,5,-1,-1,-1,-1],[-1,-1,-1,-1,6,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,2,3,-1,-1,-1,-1,-1,-1],[-1,-1,-1,7,-1,9,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1]])

def getGrilleIdiote():
    return [[1,2,3,0,0,0,0,0,0],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

def getGrillePossible():
    return [
                [2,9,-1,-1,-1,3,-1,-1,6],
                [-1,5,6,2,-1,9,3,-1,-1],
                [-1,-1,7,-1,6,5,-1,-1,2],
                [5,7,-1,-1,-1,2,4,-1,-1],
                [-1,2,3,-1,1,-1,7,5,-1],
                [8,-1,9,5,-1,-1,2,3,-1],
                [-1,4,-1,-1,-1,1,-1,7,3],
                [6,1,-1,-1,-1,4,-1,2,6],
                [-1,3,5,-1,-1,-1,8,1,4]]


def removeValuesFromList(listA, listB):
    return list(set(listA) - set(listB))
    
class Grille:
    def __init__(self):
        self.grilleData = getEmptyGrille()
        self.tailleBloc = 3
        self.noValue = -1
        self.possibleValues = [1,2,3,4,5,6,7,8,9]

        self.acceptedValues = self.possibleValues.copy()
        self.acceptedValues.append(self.noValue)

        self.gridLength = 9
        self.gridHeight = 9
        self.solution = []


    def setGrille(self, grille2D):
        self.grilleData = deepcopy(grille2D)

    def getGrille(self):
        return self.grilleData

    def printGrille(self, grille=None):
        if grille is None:
            grille = self.grilleData
            print("grilleData : ")
        noLigne = 0
        for ligne in grille:
            noLigne = noLigne+1
            for i in range(0,7,3):
                print ("[", end="")
                self.printCell(ligne[i])
                self.printCell(ligne[i+1])
                self.printCell(ligne[i+2])
                print("]", end="")
                # separateur de colonne
                if(i!=6):
                    print("    ", end="")
            print()
            # separateur de blocs
            if(noLigne%self.tailleBloc==0):
                print()

    def printSolution(self):
        print("grilleSolution : ")
        self.printGrille(self.solution)


    def printCell(self, cellValue):
        if(cellValue == self.noValue):
            print(" ", end="")
        else:
            print(cellValue, end="")

    def printCell(self, cellValue):
        if(cellValue == self.noValue):
            print(" ", end="")
        else:
            print(cellValue, end="")


    def solve(self):
        self.solution = deepcopy(self.grilleData)
        for i in range(100):
            previousSolution = deepcopy(self.solution)
            self.solveIteration(self.solution)
            nextSolution = deepcopy(self.solution)

            if(self.GridAreIdenticals(previousSolution, nextSolution)):
                return

    def GridAreIdenticals(self, grille1, grille2):
        """
        a utiliser avant une iteration de solve pour eviter de tenter de solve si l'iteration d'avant n'a pas marché
        """
        return grille1 == grille2


    # update self.solution si il y a des cases evidentes qui peuvent etre remplies
    def solveIteration(self, grille):
        for y in range(self.gridHeight):
            for x in range(self.gridLength):
                if(self.solution[y][x] == self.noValue):
                    obviousAnswer = self.getObviousAnswerOrFalse(grille, x, y)
                    if(obviousAnswer != False):
                        self.solution[y][x] = obviousAnswer


    # renvoie la valeur évidente si une seule valeur est possible ou renvoie false sinon
    def getObviousAnswerOrFalse(self, grille, posCellx, posCelly):
        possibleValues = self.getPossibleValues(grille, posCellx, posCelly)
        if(len(possibleValues) == 1):
            return possibleValues[0]
        return False

    def getPossibleValues(self, grille, posCellx, posCelly):
        """
        renvoie les valeurs possibles pour une cellule ( toutes les valeurs - valeurs existantes dans la meme ligne, colonne, bloc)
        """
        valuesAvailableForCell = self.possibleValues
        valuesAvailableForCell = removeValuesFromList(valuesAvailableForCell, self.ValuesInLine(grille, posCelly))
        valuesAvailableForCell = removeValuesFromList(valuesAvailableForCell, self.valuesInColumn(grille, posCellx))
        valuesAvailableForCell = removeValuesFromList(valuesAvailableForCell, self.valuesInBlock(grille, posCellx, posCelly))
        return valuesAvailableForCell

    def ValuesInLine(self, grille, posCelly):
        """
        renvoie l'ensemble des valeurs d'une ligne
        """
        lineToCheck = grille[posCelly]
        valuesInLine = []
        for cellValue in lineToCheck:
            if cellValue not in valuesInLine and cellValue != self.noValue:
                valuesInLine.append(cellValue)
        return valuesInLine

    
    def valuesInColumn(self, grille, posCellx):
        """
        renvoie l'ensemble des valeurs d'une colonne
        """
        valuesInColumn = []
        for line in grille:
            CellToCheck = line[posCellx]
            if CellToCheck not in valuesInColumn and CellToCheck != self.noValue:
                valuesInColumn.append(CellToCheck)
        return valuesInColumn
    
    def valuesInBlock(self, grille, posCellx, posCelly):
        """
        renvoie l'ensemble des valeurs d'un block
        """
        valuesInBlock = []
        posTopRightCorner = self.getBlockTopLeftCorner(posCellx, posCelly)
        for y in range(posTopRightCorner.y, posTopRightCorner.y+self.tailleBloc):
            for x in range (posTopRightCorner.x, posTopRightCorner.x+self.tailleBloc):
                CellToCheck = grille[y][x]
                if CellToCheck not in valuesInBlock and CellToCheck != self.noValue:
                    valuesInBlock.append(CellToCheck)
        return valuesInBlock 

    def getBlockTopLeftCorner(self, posCellx, posCelly):
        posTopRightCorner = Position(math.floor(posCellx/self.tailleBloc)*self.tailleBloc, math.floor(posCelly/self.tailleBloc)*self.tailleBloc)
        return posTopRightCorner

