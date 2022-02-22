# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 00:52:10 2022

@author: Gimena Navarrete
"""
booleanos = [True,False]

print("Representar la tabla logica [(p->q)^(-q^r)] v (p<=>r)")
print()
print("  p   |\t  q   |\t  r   \tp->q   -q\t\tp<=>r\t-q ^ r\t| [(p->q)^(-q^r)]\t[(p->q)^(-q^r)] v p<=>r")
print("-"*100)

t = True


for p in booleanos:
    for q in booleanos:
        for r in booleanos:
            if p == True and q == False:
                t = False
            if p == False:
                t = True
                
            print(p,
                  q,
                  r,
                  t,
                  not q,
                  p is r,
                  not q and r,
                  (t) and (not q and r),
                  ((t) and (not q and r)) or (p is r),
                  sep='\t  ')
    