# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:22:25 2023

@author: clara
"""
import interface_etendue as ie

l = [(1, 0),(2, 2),(1, 1),(4, 0),(10, 0),(3, 10)]


dico_test = ie.make(l)
print(dico_test)
print(ie.mem(dico_test,1))
print(ie.size(dico_test))
print(ie.keys(dico_test))
print(ie.map(dico_test, ie.f))
print(ie.clear(dico_test))