def final(rank1,perc,category,state,gender,pwd):
    import pandas as pd
    import numpy as np

    import csv
    from pathlib import Path

    base_path = Path(__file__).parent
    file_path = (base_path / "..//app//round1_cleaned.csv").resolve()


    df=pd.read_csv(file_path)
    if(rank1=='-1'):
        rank=float(pvr(perc,pwd,category))
    else:
        rank=rank1
    if(pwd=='YES'):
        if(gender=='M'):
            catg=category+'-PwD'
            p=df[(df['Closing Rank']>=rank)&((df['Category']==catg)|(df['Category']=='OPEN-PwD'))&(df['Seat Pool']=='Gender-Neutral')]
        else:
            catg=category+'-PwD'
            p=df[(df['Closing Rank']>=rank)&((df['Category']==catg)|(df['Category']=='OPEN-PwD'))]
    else:
        if(gender=='M'):
            p=df[(df['Closing Rank']>=rank)&((df['Category']==category)|(df['Category']=='OPEN'))&(df['Seat Pool']=='Gender-Neutral')]
        else:
             p=df[(df['Closing Rank']>=rank)&((df['Category']==category)|(df['Category']=='OPEN'))]
    v=[]
    for i in p.index:
        if(p['State'][i]==state):
            if(p['Quota'][i]=='OS'):
                v.append(i)
        elif((p['State'][i]!='All India')&(p['State'][i]!=state)):
            if(p['Quota'][i]=='HS'):
                v.append(i)
    q=p.drop(index=v)
    q=q.sort_values('Branch Name')
    # klaus=q[(q['Branch Name']=='CS')|(q['Branch Name']=='IT')|(q['Branch Name']=='ME')|(q['Branch Name']=='ECE')|(q['Branch Name']=='CSE')]
    klaus=q;
    klaus.reset_index(drop=True,inplace=True);

    return klaus.drop(['Quota','Category','Seat Pool','Opening Rank','Closing Rank','State'],axis=1)
