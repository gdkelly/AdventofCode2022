# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:06:31 2022

@author: Greg.Kelly
"""
import pandas as pd
data=open('day2_input.txt','r')
df=pd.read_csv('day2_input.txt',header=None,sep=' ')
score=0
values={'X':[1,'A','B','C'],'Y':[2,'B','C','A'],'Z':[3,'C','A','B']}
for i in range(0,len(df)):
    my_pick = df[1][i]
    opponent_pick=df[0][i]
    if opponent_pick == values[my_pick][1]:
        print('draw')
        score+=values[my_pick][0] + 3
    if opponent_pick == values[my_pick][2]:
        print('loss')
        score+=values[my_pick][0]
    if opponent_pick == values[my_pick][3]:
        print('win')
        score+=values[my_pick][0]+6
    print(i)
    print(score)