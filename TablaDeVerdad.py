# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 00:52:10 2022

@author: Gimena Navarrete
"""
booleanos = [True,False]

print("Representar la tabla logica [(p->q)^(-q^r)] v (p<=>r)")
print()
print("-"*108)
print("  p\t\t\t\t\t\t  r\t\t\t\t\t\t -q\t\t\t\t\t\t-q^r\t[(p->q)^(-q^r)]")
print("-"*108)

t = True


for p in booleanos:
    for q in booleanos:
        for r in booleanos:
            
            print(p,
                  q,
                  r,
                  not p or q,
                  not q,
                  p is r,
                  not q and r,
                  (not p or q) and (not q and r),
                  ((not p or q) and (not q and r)) or (p is r),
                  sep='\t\t')
print("-"*108)
print("\t\t\t  q\t\t\t\t\t\tp->q\t\t\t\t\tp<=>r\t\t\t\t   [(p->q)^(-q^r)]v(p<=>r)")
print("-"*108)