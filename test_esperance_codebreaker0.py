# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:59:36 2023

@author: clara
"""

import codebreaker0
import codebreaker1
import codebreaker2
import codemaker1
import codemaker2
import play
import common 
from matplotlib import pyplot as plt

#evaluation_p = None
#combinaison = codebreaker.codebreaker(evaluation_p)
#print(combinaison)

#print(play.play(codemaker1,codebreaker0, quiet=True))


                

def esperance (play,codemaker, codebreaker, k):
    nb_essai = []
    E = 0
    L = [0]*k
    maxi = 0
    somme = 0
    P = [0]*k 
    for n in range(k):
        nb_E = play.play(codemaker,codebreaker, quiet=True)
        if nb_E not in nb_essai :
            nb_essai.append(nb_E)
        #if maxi <= nb_E :
       #     maxi = nb_E 
       # somme += nb_E
        
        for i in range(len(nb_essai)):
            if nb_essai[i] == nb_E :
                indice = i
                
        L[indice] += 1      
    print(nb_essai)        
      
    print(L)
    
    for i in range(len(P)):
            P[i] = L[i]/k  
    print(P)    
    #return nb_essai
    n, bins, patches = plt.hist(nb_essai, color='blue', edgecolor='black', )
    plt.xlabel('nombre d essais')
    plt.ylabel('nb de joueurs gagnant avec ce nombre d essais')
    plt.title('répartition du nombre d essais necessaires')
    plt.legend()
    plt.show()
    
    for i in range(len(P)):
         E += P[i]*nb_essai[i]
    print('l esperance du nombre d essai est de',E,'essais')
        
    
#esperance(play,codemaker1, codebreaker0, 100)
#esperance(play,codemaker1, codebreaker1, 100)
#esperance(play,codemaker1, codebreaker2, 5)
esperance(play,codemaker2, codebreaker0, 100)

def comparer(codemaker, codebreaker_0, codebreaker_1, k):
    nb_essai_0 = 0
    nb_essai_1 = 0
    
    tot_essai_0 = []
    tot_essai_1 = []
    x = []
    for n in range(k) :
        
        nb_essai_0 += play.play(codemaker,codebreaker0, quiet=True)
        tot_essai_0.append(nb_essai_0) 
        
        nb_essai_1 += play.play(codemaker,codebreaker1, quiet=True)       
        tot_essai_1.append(nb_essai_1) 
        x.append(n)
        
    plt.plot(x,tot_essai_0, label='codebreaker0')
    plt.plot(x, tot_essai_1, label = 'codebreaker1')
    plt.xlabel('nombre de parties')
    plt.ylabel('nombre d essais cumulés')
    plt.title('nombre d essais cumulés en fonction du nombre de parties')           
    plt.legend()
    
comparer(codemaker1, codebreaker0, codebreaker1, 5)

        
        
        
    
        
        
    








    