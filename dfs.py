# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 19:01:47 2022

@author: aynur
"""

grafik={'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':['I','İ','J'],
        'E':['K','L'],
        'F':['M','N'],
        'G':[],
        'I':[],
        'İ':[],
        'J':[],
        'K':[],
        'L':[],
        'M':[],
        'N':[],
        
        }
ziyaret=set()#ziyaret kümemiz

def dfs(ziyaret, grafik, dügüm):
    if dügüm not in ziyaret:
        print(dügüm)
        ziyaret.add(dügüm)
        for komsu in grafik[dügüm]:
            dfs(ziyaret, grafik, komsu)
dfs(ziyaret, grafik, 'A')