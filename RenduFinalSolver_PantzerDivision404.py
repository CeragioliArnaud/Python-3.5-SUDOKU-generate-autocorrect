# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:45:45 2016

@author: ca503907
"""

nb_methodes=1
def resolution(A, methode=0):
    A1=[[]]
    A2=[[]]
    if methode==1:    
        	
        SudPrint(A)
    
        if resolveTab(A):
            SudPrint(A)
            A1=resolveTab(A)
    
    if methode==0:    
        	
                
        ImpressionTab(A)
        A2=Resolveur(A)
    
    B=[A1,A2]
    return B
            
            
"""*-------***--------SOLVER 0, le moins optimal------***--------*"""            
            
            
def SudPrint(LeTab):
    
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
     
     
def resolveTab(LeTab):
    "Résoud, si possible, la grille de sudoku"
         
         
    def CheckRow(i):
        "Vérification d'une ligne"
        numbers = [False]*10
        for j in range (9):
            number = LeTab [i][j]
            if number != 0:
                if numbers [number]:
                    return False
                numbers [number] = True
        return True
         
         
    def CheckColumn(j):
        "Vérification d'une colonne"
        numbers = [False]*10
        for i in range (9):
            number = LeTab [i][j]
            if number != 0:
                if numbers [number]:
                    return False
                numbers [number] = True
        return True
         
    def CheckSquare(i, j):
        "Vérification d'un carré"
        numbers = [False]*10
        x , y = (j //3) * 3 , (i //3) * 3
        for i in range (y , y + 3):
            for j in range (x , x + 3):
                number = LeTab [i][j]
                if number != 0:
                    if numbers [number]:
                        return False
                    numbers [number] = True
        return True
         
    def CheckPoss(i, j, val):
        "Vérification d'un coup"
        old , LeTab [i][j] = LeTab [i][j] , val
        if not CheckRow (i) or not CheckColumn (j) or not CheckSquare (i, j):
            LeTab [i][j] = old
            return False
        LeTab [i][j] = old
        return True
         
    def resolveTabRec(i, j):
        "Résolution récursive"
        while LeTab [i][j] != 0:
            j += 1
            if j > 8:
                j = 0
                i += 1
                if i > 8:
                    return True
             
        for number in list(range(4,10))+ list(range(1,4)):
            if CheckPoss (i, j,number):
                LeTab [i][j] = number
                if resolveTabRec (i, j):
                    return True
        LeTab [i][j] = 0
        return False
     
         
    return resolveTabRec(0, 0)
     
"""*-----------------------------------------------------------------*"""      
   
"""*-------***-------SOLVER 1, le plus optimisé--------***--------*"""      

def TabRempli(LeTab):
    for x in range(0, 9):
        for y in range (0, 9):
            if LeTab[x][y] == 0:
                return False
    return True
    

def Order(LeTab):
    
    C=[(len([x for x in LeTab[i] if(x!=0)]), i) for i in range (0,9)]
    C.sort()
    return [L[1] for L in C]
    
    
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
 Elle résoud et imprime le resultat sur la console
"""
def Resolveur(LeTab):
    
    i = 0
    j = 0
    
    Possibilitees = {}
    #ImpressionTab(LeTab)
    D=Order(LeTab)
    if TabRempli(LeTab):
        print("La résolution du Sudoku est un succès !!")
        ImpressionTab(LeTab)
        return True
    else: #IMPORTANT
            for x in D:
                for y in range (0, 9):
                    if LeTab[x][y] == 0:
                        i = x
                        j = y
                        break #def
                    else:
                        continue
                if LeTab[x][y] == 0:
                    break
            
              
            Possibilitees = Check(LeTab, i, j)
            
            #Test de toutes les possibilitées
            for x in range (1, 10):
                if not Possibilitees[x] == 0:
                    LeTab[i][j] = Possibilitees[x]
                    if (Resolveur(LeTab)):
                        return True
            LeTab[i][j] = 0
            return False
        
"""Ceci est la fonction 'ImpTabF'"""
#Impression sudoku + esthetique
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
    
    
"""*-----------------------------------------------------------------*"""          
    
    
    
    
    
    