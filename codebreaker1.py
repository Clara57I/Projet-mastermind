# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:59:51 2023

@author: clara
"""

import random
import common 



def init():
    tried = []       
    return tried

tried = []
evaluation_p = None
rep = 0


def codebreaker(evaluation_p) :
    global tried
    global rep
    combinaison = random.choices(common.COLORS, k=common.LENGTH)  
    
    while combinaison in tried :
        combinaison = random.choices(common.COLORS, k=common.LENGTH)
        return None
        
    tried.append(''.join(combinaison))
    return ''.join(combinaison)  
   
        

print(codebreaker(evaluation_p))

###############################################################################

        
# #%% Au lieu de partir sur la sauvegarde de ce qu'on a déjà essayé
# # On peut plutot reduire le champ des possibles au fur et à mesure.


# not_tried = None # Une liste des propositions pas encore essayé
# def init():
#     global not_tried
#     not_tried = list(common.solutions_possibles) # Je récupère une *copie* de l'ensemble des solutions possibles
#     random.shuffle(not_tried) # Je melange l'ensemble *not_tried* et non *solution_possibles*.
#     return not_tried

# def codebreaker(evalution_precedente):
#     global not_tried
#     solution_proposee = not_tried.pop()
#     # L'opération pop reduit la taille de not_tried donc aucune chance que la
#     # meme combinaison soit rejouée une seconde fois.
#     return solution_proposee





        

        
