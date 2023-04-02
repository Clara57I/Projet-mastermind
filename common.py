#!/usr/bin/env python3

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']

from itertools import combinations_with_replacement as cwr
solutions_possibles = (list(cwr(COLORS,4)))

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

# print(evaluation(['R','R','V','B'],['J','O','R','V']))
# print(evaluation(['B','O','M','G'],['B','B','J','O']))
# print(evaluation(['R','R','V','B'],['B','B','J','O']))
# print(evaluation(['J','J','R','R'],['J','J','O','O']))

# #créer la liste de toutes les combinaisons possibles 
# from itertools import combinations_with_replacement as cwr
# solutions_possibles = (list(cwr(COLORS,4))) 

# #print((solutions_possibles))
# #print(evaluation(['B','B','J','O'],solutions_possibles[6]))

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
    print('nb solutions possibles avant',len(ensemble_sol))
    for sol in ensemble_sol :  
            bp,mp = (evaluation(sol, combinaison_test))       
            if (bp,mp) != ev :   
                eff.append(sol) #on créee une liste pour stocker les solutions non possibles
    #return eff
    for i in range(len(eff)):
        if eff[i] in ensemble_sol : #on enlève de l'ensemble les solutions non possibles
            ensemble_sol.remove(eff[i])
    print('nb solutions possibles après',len(ensemble_sol)) 
    return ensemble_sol
                

print(ensemble_sol)    
print(maj_possibles(ensemble_sol,['V','J','O','O'],(2,0)))
print(maj_possibles(ensemble_sol,['B','O','J','G'],(2,2)))
print(ensemble_sol)

####################################################################################################
# def evaluation(solution, combinaison) :
#     bp = 0
#     mp = 0    
#     varcombi = [0]*4   #Liste pour indiquer si une lettre de la combinaison a déja été vérifiée ou pas
#     varsolu = [0]*4    #Liste pour indiquer si une lettre de la solution a déja été comparée avec la combinaison ou pas
    
#     for i in range(LENGTH) :
#         for j in range(LENGTH) :
#             if combinaison[j]==solution[i]: #On vérifie que c'est la bonne lettre
#                 if i == j :    #On vérifie que cette bonne lettre est à la bonne position                
#                     bp += 1    #On ajoute 1 au compteur des lettres bien placées
#                     varcombi[j] = 'None'
#                     varsolu[i] = 'Fait'
#                 if varcombi[j] != 'None' and varsolu[i] != 'Fait' :                  
#                     mp +=1
#                     varcombi[j] = 'None'
#                     varsolu[i] = 'Fait'
                    
#     return(bp,mp)

# print(evaluation(['R','R','V','B'],['J','O','R','V']))
# print(evaluation(['B','O','M','G'],['B','B','J','O']))
# print(evaluation(['R','R','V','B'],['B','B','J','O']))
# print(evaluation(['J','J', 'R','R'],['J','J','O','O']))


# from itertools import combinations_with_replacement as cwr
# solutions_possibles = set(cwr(COLORS,4))
#solutions_possibles = set([x+y+z+t for x in COLORS for y in COLORS for z in COLORS for t in COLORS])

#print(len((solutions_possibles)))
#print(evaluation(['B','B','J','O'],solutions_possibles[6]))
#%%QUESTION 5

# A discuter avec Clara : on m'a dit que faire des lectures et écritures
# provoquent des erreurs difficiles à detecter.

# def donner_possibles(combinaison_test, ev):
#     global solutions_possibles
#     for sol in solutions_possibles :  
#         bp,mp = (evaluation(combinaison_test,sol))       
#         if (bp,mp) != ev :            
#             solutions_possibles.remove(sol)
#     return set(solutions_possibles)

# def donner_possibles(combinaison_test, evaluation_test):
#     possibles = set()
#     global solutions_possibles
#     for sol in solutions_possibles:
#         eval_sol = evaluation(combinaison_test, sol)
#         if eval_sol == evaluation_test:
#             possibles.add(sol)
#     return possibles

#print(donner_possibles('RRRR', (1, 0)))
#donner_possibles(['B','B','J','O'], (1,2))
#print(evaluation(['B','B','J','O'],solutions_possibles[5]))    
#print(donner_possibles(['B','B','J','O'], (1,2)))
#print(len(donner_possibles(['B','B','J','O'], (1,2))))
#%%QUESTION 6

# En conséquence de la modification de *donner_possible**
# def maj_possibles(solutions_possibles,combinaison_test,ev):    
#     return list(donner_possibles(combinaison_test, ev))

# def maj_possibles(solutions_possibles_avant_essai, combinaison_test, evaluation_test):
#     possibite_apres_essai = donner_possibles(combinaison_test, evaluation_test)
#     solutions_possibles_avant_essai.intersection_update(possibite_apres_essai)
#     return

#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['B','B','J','O'],(0,3))
#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['O','J','J','B'],(2,3))
#print(len(solutions_possibles))
#maj_possibles(solutions_possibles,['0','J','B','J'],(3,4))
#print(len(solutions_possibles))
#print(maj_possibles(solutions_possibles,['0','J','B','M'],(0,4)))
#print(len(solutions_possibles))
