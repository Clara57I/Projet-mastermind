# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:04:14 2023

@author: clara
"""

import play
import common
import codemaker1
import codebreaker1


print 
def check(codemaker, codebreaker):
    
    global solution
    first_solution = codemaker.init()
    
    play.play(codemaker, codebreaker, quiet=True)     
    
    if solution != first_solution :
        print('triche')
        
check(codemaker1, codebreaker1)


    
    

    
    