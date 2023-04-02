# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:25:10 2023

@author: clara
"""

import common
import sys
import random


def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    return solution

def evaluation_complete(solution, combinaison):
    """
    Cette fonction n'est pas correcte, elle n'implémente qu'une évaluation partielle
    """
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    (bp,mp) = common.evaluation(solution, combinaison)
    return(bp, mp)

def codemaker(combinaison):
    global solution
    #solution = init()   
    (bp,mp) = evaluation_complete(solution, combinaison)
    return (bp,mp)

    if mp >= 3 or bp >= 3 :
        L = common.donner_solutions(common.combinaison_test, common.ev)
        solution = random.choice(L)
        
        
solution = ['B','B','J','O']
print(codemaker(['B','B','J','O']))
            
            
    
