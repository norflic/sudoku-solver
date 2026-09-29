
class Grille:
    def __init__(self):
        self.grilleData = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        self.tailleBloc = 3
        self.noValue = -1


    def setGrille(self, grille2D):
        self.grilleData = grille2D

    def getGrille(self):
        return self.grilleData



    def printGrille(self):
        noLigne = 0
        for ligne in self.grilleData:
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

    def printCell(self, cellValue):
        if(cellValue == self.noValue):
            print(" ", end="")
        else:
            print(cellValue, end="")
