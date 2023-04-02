# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:35:43 2023

@author: clara
"""

import common 
import random
global ensemble_sol
global solution


import codemaker0
import codemaker1
import codemaker2



from itertools import combinations_with_replacement as cwr
solutions_possibles = (list(cwr(common.COLORS,4)))

# def init(): 
#    combinaison_test = random.choices(common.COLORS, k = common.LENGTH) 
#    ev = common.evaluation(solution, combinaison_test)
#    ensemble_sol = common.donner_solutions(combinaison_test,ev)
#    return ensemble_sol

# #donnée par codemaker
solution = codemaker1.init()


def init():
    global ensemble_sol
    global solution
    global ev
    global tried
    
    combinaison_test = random.choices(common.COLORS, k=common.LENGTH)
    #print('comb test',combinaison_test)  
    ev = common.evaluation(solution, combinaison_test)
    tried = []
    ensemble_sol = common.donner_solutions(combinaison_test,ev)
    return ensemble_sol



# #print('ensemble solutions possibles',ensemble_sol)
# ensemble_sol = init()

# def codebreaker(ev):
    
#     global combinaison
#     global ensemble_sol 

    
#     combi=""
       
#     #print('ensemble sol', ensemble_sol)   
    
#     #mise à jour de ensemble_sol d'après combinaison précedente
#     if ev :
#         if tried :            
#          dernier_essai = tried[len(tried)-1]
#          ensemble_sol = common.maj_possibles(ensemble_sol,dernier_essai,ev)
#          print('dernier_essai',dernier_essai)
#          print('ensemble sol',ensemble_sol) 
    
#     #choisir aléatoirement une solution dans la liste des solutions possibles
#     combinaison_test = random.choices(list(ensemble_sol))
#     combinaison = list(combinaison_test[0])
    
#     tried.append(combinaison)
#     #print(tried)
        
#     for i in range(len(combinaison)):
#         combi += combinaison[i]  
        
#    #ev = common.evaluation(solution, combinaison_test)
   
#     #print('ensemble sol',len(ensemble_sol))
          
#     return combi
       
# print(codebreaker((None)))
# print(codebreaker((0,3)))
# # print(codebreaker((0,3)))
# # print(tried[len(tried)-1])

###############################################################################
combinaison_test = init()   
def codebreaker(ev):
    global combinaison_test
    global solutions_possibles
    global ensemble_sol
    
    sol=""
    L = []  
    if list(ensemble_sol) :             
        comb = random.choices(list(ensemble_sol))
    
        print("la longueur de l'ensemble des solutions", len(ensemble_sol))
    # print('comb',comb)
    # print(comb[0][0])
    # print(comb[0])
        for i in range(len(comb[0])) :
            L.append(comb[0][i]) 
            print("coucou")
  
        for i in range(len(L)):
            sol += L[i]
            print("coucou2")

         
        combinaison_test = L
        print("L est ", L, "combi test ", combinaison_test)
        eva = common.evaluation(solution, combinaison_test)
        print("eva est ", eva)
        solutions_possibles_avant_essai = ensemble_sol
        print("sol possible avant essai est ", solutions_possibles_avant_essai)
        ensemble_sol = list(common.maj_possibles(solutions_possibles_avant_essai, combinaison_test, eva))
        print("l'ensemble des solutions",(ensemble_sol))
       
        return sol
        
    else :
        print('liste vide')

print('solution',solution)  
codebreaker((1,2))
codebreaker((1,0))
codebreaker((2,0))

#print('comb test',combinaison_test)  
        
# print(codebreaker((1,2)))
    
    

