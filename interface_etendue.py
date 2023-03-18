# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:14:37 2023

@author: clara
"""


import dico_triees as dico

def make(l):
    d = dico.empty()
    for (k,v) in l :
        dico.add(d,k,v)
    return d
            

def mem(d,clé):
    if dico.find(d, clé) == None :
        return False
    return True
           

def size(d):
    return len(dico.items(d))
    
    
def keys(d):
    L = dico.empty()
    for (k,v) in d :
      dico.add(L,k,None)
    return L
   
def f(x):
    return 2*x

def map(d,f):
    resultat= dico.empty()
    for (k,v) in d :
        nv = f(v)
        dico.remove(d,k)
        dico.add(resultat,k, nv)  
    return resultat
    

def clear(d):
    for (k,v) in d:
        dico.remove(d,k)
    return d

l = [(1, 0),(2, 2),(1, 1),(4, 0),(10, 0),(3, 10)]

dico_test = make(l)
#print(dico_test)
#print(mem(dico_test,1))
#print(size(dico_test))
#print(keys(dico_test))
#print(map(dico_test, f))
#print(clear(dico_test))

    