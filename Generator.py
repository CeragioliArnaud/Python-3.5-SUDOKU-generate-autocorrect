"""
I=Ligne
J=Colonne

TEAM : PantZer Division 404 
"""
import random

def MatriceR():
    M =[[0 for i in range(0,9)] for j in range(0,9)]
    for z in range(0,22):
        pointRandom(M)
    Resolveur(M)
    
    if (Resolveur(M)==True):
        
        print('La création du SUDOKU est un succès!!!')
        ImpressionTab(M)
        
    else:
        
        MatriceR()
    
        
def pointRandom(M):
    a = random.randint(0,8)
    b = random.randint(0,8)
    if M[a][b]==0:
        M[a][b]= random.randint(1,9)
        if checkPoint(M, a, b)==False:
            M[a][b]= 0
    else :
        pointRandom(M)
    
"""Partie Resolv"""
def TabRempli(LeTab):
    for x in range(0, 9):
        for y in range (0, 9):
            if LeTab[x][y] == 0:
                return False
    return True
    
    

def Check(LeTab, i, j):
    
    LeTabPossibilitee= {}
    
    for x in range (1, 10):
        LeTabPossibilitee[x] = 0
    
    #L'Horizonnalité
    for y in range (0, 9):
        if not LeTab[i][y] == 0: 
            LeTabPossibilitee[LeTab[i][y]] = 1
     
    #La Verticalité
    for x in range (0, 9):
        if not LeTab[x][j] == 0: 
            LeTabPossibilitee[LeTab[x][j]] = 1
            
    #Les carrées 3x3 du SUDOKU
    # PARTIE ULTRA CHIANTE A CODER n°1, MERCI LES MATHS
    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6
    for x in range (k, k + 3):
        for y in range (l, l + 3):
            if not LeTab[x][y] == 0:
               LeTabPossibilitee[LeTab[x][y]] = 1          
    
    for x in range (1, 10):
        if LeTabPossibilitee[x] == 0:
            LeTabPossibilitee[x] = x
        else:
            LeTabPossibilitee[x] = 0
    
    return LeTabPossibilitee


""" Ceci est la fonction 'Resolveur'
 Elle résout et imprime le resultat sur la console
"""
def Resolveur(LeTab):
    
    i = 0
    j = 0
    
    Possibilitees = {}
    #ImpressionTab(LeTab)
    
    if TabRempli(LeTab):
        return True
    else: #PARTIE ULTRA CHIANTE A CODER n°2
        for x in range (0, 9):
            for y in range (0, 9):
                if LeTab[x][y] == 0:
                    i = x
                    j = y
                    break #def
                else:
                    continue
            if LeTab[x][y] == 0:
                break
        
       #s rien=input()    
        Possibilitees = Check(LeTab, i, j)
        
        #Test de toutes les possibilitées
        for x in range (1, 10):
            if not Possibilitees[x] == 0:
                LeTab[i][j] = Possibilitees[x]
                if (Resolveur(LeTab)):
                    return True
        LeTab[i][j] = 0
        return False
        
"""Fin resolv part """
def checkPoint(M, a, b):
    i = a
    j = b  
    #Test en Ligne
    for j in range(0,9):
        if j!=b:
            if M[a][j]==M[a][b]:
                return False
    #Test en Colonne
    for i in range(0,9):
        if i!=a:
            if M[i][b]==M[a][b]:
                return False
    #Test en carré
    k = a//3
    l = b//3
    for j in range(l*3, l*3+3):
        for i in range(k*3, k*3+3):
            if j!=b:
                if i!=a:
                    if M[i][j]==M[a][b]:
                        return False
    return True
    
def ImpressionTab(LeTab):
    print("*-------*-------*-------*")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("*-------*-------*-------*")
        print("| ",end="")
        for y in range(0, 9):
            if y == 3 or y == 6 or y==9:
                print("|", end=" ")
            print(LeTab[x][y], end=" ")
        print("|")
    print("*-------*-------*-------*")
    
MatriceR()