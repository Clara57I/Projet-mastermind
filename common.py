#!/usr/bin/env python3

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

#print(COLORS[0])
#%%QUESTION 1
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

#print(evaluation(['R','R','V','B'],['J','O','R','V']))
#print(evaluation(['B','O','M','G'],['B','B','J','O']))
#print(evaluation(['R','R','V','B'],['B','B','J','O']))
#print(evaluation(['J','J', 'R','R'],['J','J','O','O']))


from itertools import combinations_with_replacement as cwr
solutions_possibles = list(cwr(COLORS,4))
#solutions_possibles = [x+y+z+t for x in COLORS for y in COLORS for z in COLORS for t in COLORS]

#print(len((solutions_possibles)))
#print(evaluation(['B','B','J','O'],solutions_possibles[6]))
#%%QUESTION 5
def donner_possibles(combinaison_test, ev):
    global solutions_possibles
    for sol in solutions_possibles :  
        bp,mp = (evaluation(combinaison_test,sol))       
        if (bp,mp) != ev :            
            solutions_possibles.remove(sol)
    return set(solutions_possibles)

#print(donner_possibles('RRRR', (1, 0)))
#donner_possibles(['B','B','J','O'], (1,2))
#print(evaluation(['B','B','J','O'],solutions_possibles[5]))    
#print(donner_possibles(['B','B','J','O'], (1,2)))
#print(len(donner_possibles(['B','B','J','O'], (1,2))))
#%%QUESTION 6
def maj_possibles(solutions_possibles,combinaison_test,ev):    
    return list(donner_possibles(combinaison_test, ev))

#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['B','B','J','O'],(0,3))
#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['O','J','J','B'],(2,3))
#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['0','J','B','J'],(3,4))
#print(len(solutions_possibles))
#print(maj_possibles(solutions_possibles,['0','J','B','M'],(0,4)))
#print(len(solutions_possibles))



    
        
    
    

            
