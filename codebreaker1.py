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
        

#print(codebreaker(evaluation_p))


        