#!/usr/bin/env python3

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

#print(COLORS[0])

def evaluation(solution, combinaison) :
    bp = 0
    mp = 0    
    varcombi = [0]*4
    varsolu = [0]*4
    
    for i in range(LENGTH) :
        for j in range(LENGTH) :
            if combinaison[j]==solution[i]: 
                if i == j :                    
                    bp += 1
                    varcombi[j] = 'None'
                    varsolu[i] = 'Fait'
                if varcombi[j] != 'None' and varsolu[i] != 'Fait' :                  
                    mp +=1
                    varcombi[j] = 'None'
                    varsolu[i] = 'Fait'
                    
    return(bp,mp)

print(evaluation(['R','R','V','B'],['J','O','R','V']))
print(evaluation(['B','O','M','G'],['B','B','J','O']))
print(evaluation(['R','R','V','B'],['B','B','J','O']))
print(evaluation(['J','J','R','R'],['J','J','O','O']))

#créer la liste de toutes les combinaisons possibles 
from itertools import combinations_with_replacement as cwr
solutions_possibles = (list(cwr(COLORS,4))) 

#print((solutions_possibles))
#print(evaluation(['B','B','J','O'],solutions_possibles[6]))

def donner_solutions(combinaison_test, ev):
    global solutions_possibles
    global ensemble_sol 
    
    ensemble_sol = set()
    #print('nb solutions possibles avant',len(solutions_possibles))
    for sol in solutions_possibles :  
        bp,mp = (evaluation(sol, combinaison_test))       
        if (bp,mp) == ev :    
            ensemble_sol.add(sol)
        
    #print('nb solutions possibles après',len(ensemble_sol))  
    return ensemble_sol  
    

  
print(donner_solutions(['B','B','J','O'], (1,2)))
  

ensemble_sol = donner_solutions(['B','B','J','O'], (1,2))

def maj_possibles(ensemble_sol,combinaison_test,ev): 
    
    eff = []     
    #print('nb solutions possibles avant',len(ensemble_sol))
    for sol in ensemble_sol :  
            bp,mp = (evaluation(sol, combinaison_test))       
            if (bp,mp) != ev :   
                eff.append(sol) #on créee une liste pour stocker les solutions non possibles
    #return eff
    for i in range(len(eff)):
        if eff[i] in ensemble_sol : #on enlève de l'ensemble les solutions non possibles
            ensemble_sol.remove(eff[i])
    #print('nb solutions possibles après',len(ensemble_sol)) 
    return ensemble_sol
                

print(ensemble_sol)    
print(maj_possibles(ensemble_sol,['V','J','O','O'],(2,0)))
print(maj_possibles(ensemble_sol,['B','O','J','G'],(2,2)))
print(ensemble_sol)




    
        
    
    

            
