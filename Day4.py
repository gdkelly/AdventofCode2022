# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:10:12 2022

@author: Greg
"""

data=open('input.txt','r')
pairs=data.read().splitlines()
value=0

def split(pair):
    pair_list=pair.split('-')
    start_1=pair_list[0]
    end_1=pair_list[1].split(',')[0]
    start_2=pair_list[1].split(',')[1]
    end_2=pair_list[2]
    pairs_list=[int(start_1),int(end_1),int(start_2),int(end_2)]
    
    check=any_check(pairs_list)
    if check ==True:
        return True
    
def range_check(pairs_list):
    set_1=set(range(pairs_list[0],pairs_list[1]+1))
    set_2=set(range(pairs_list[2],pairs_list[3]+1))
    if set_1.issubset(set_2):
        return True
    elif set_2.issubset(set_1):
        return True
    else:
        return False

def any_check(pairs_list):
    set_1=set(range(pairs_list[0],pairs_list[1]+1))
    set_2=set(range(pairs_list[2],pairs_list[3]+1))
    if len(set_1 & set_2) >0:
        return True

for i in range(0,len(pairs)):
    a=split(pairs[i])
    if a ==True:
        value+=1

print(value)
        