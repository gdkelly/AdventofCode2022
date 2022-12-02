import pandas as pd
df=pd.read_csv('input.txt',header=None,sep=' ')
score=0
values={'X':{'init':0,'A':3,'B':1,'C':2},
        'Y':{'init':3,'A':1,'B':2,'C':3},
        'Z':{'init':6,'A':2,'B':3,'C':1}}
for i in range(0,len(df)):
    wld=df[1][i]
    opponent_pick=df[0][i]
    score+=values[wld]['init']+values[wld][opponent_pick]
print(score)
