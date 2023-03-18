# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:13:06 2023

@author: clara
"""

import common as com


import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    return solution


def evaluation_complete(solution, combinaison):
    """
    Cette fonction n'est pas correcte, elle n'implémente qu'une évaluation partielle
    """
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

solution = ['B','O','M','G']

print(codemaker(['B','B','J','O']))

