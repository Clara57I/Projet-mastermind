# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:35:43 2023

@author: clara
"""

import common 
import random
global solutions_possibles
global solution

#import codemaker0
#import codemaker1
#import codemaker2


from itertools import combinations_with_replacement as cwr
solutions_possibles = (list(cwr(common.COLORS,4)))
#print(solutions_possibles)


def init():
    combinaison_test = random.choices(common.COLORS, k=common.LENGTH)
    return combinaison_test
    
combinaison_test = init()
#print('comb test',combinaison_test)



def codebreaker(ev):
    global combinaison_test
    global solutions_possibles
    
    sol=""
    L = []                      
    comb = random.choices(solutions_possibles)
    
    for i in range(len(comb[0])) :
        L.append(comb[0][i]) 
  
    for i in range(len(L)):
        sol += L[i]  
        
    solutions_possibles = list(common.donner_possibles(combinaison_test, ev))
    combinaison_test = L
    
    return sol


codebreaker((1,2))
#print('comb test',combinaison_test)  
        
#print(codebreaker((1,2)))
    
    

