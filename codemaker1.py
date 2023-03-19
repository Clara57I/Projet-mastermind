# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:13:06 2023

@author: clara
"""

import sys
import random
import common as com # N'utilisez pas la syntaxe "from common import XXX"

solution = None # la solution est initialisée par la fonction init
def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(random.choices(com.COLORS, k=com.LENGTH))
    return solution

#%%QUESTION 2
def evaluation_complete(solution, combinaison):
  
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    (bp,mp) = com.evaluation(solution, combinaison)
    return(bp, mp)

#print(evaluation_complete(['B','O','M','G'],['B','B','J','O']))

def codemaker(combinaison):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    return evaluation_complete(solution, combinaison)


#print(codemaker(['B','B','J','O']))

