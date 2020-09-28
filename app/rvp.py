# This function is used to predict the rank using Linear Regression

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def pvr(perc,pwd,category):
    rvp = pd.read_csv('rvp_cleaned.csv')

    if(pwd == 'YES'):
        if(category == 'GEN'):
            rvp_gp = rvp[rvp['CATEGORY'] == 'GEN-PwD']
            z = predictor(perc, rvp_gp)
        elif(category == 'SC'):
            rvp_scp = rvp[rvp['CATEGORY'] == 'SC-PwD']
            z = predictor(perc, rvp_scp)
        elif(category == 'ST'):
            rvp_stp = rvp[rvp['CATEGORY'] == 'ST-PwD']
            z = predictor(perc, rvp_stp)
        elif(category == 'EWS'):
            rvp_ep = rvp[rvp['CATEGORY'] == 'EWS-PwD']
            z = predictor(perc, rvp_ep)
        else:
            rvp_obp = rvp[rvp['CATEGORY'] == 'OBC-NCL-PwD']
            z = predictor(perc, rvp_obp)
    else:
        if(category == 'GEN'):
            rvp_g = rvp[rvp['CATEGORY'] == 'GEN']
            z = predictor(perc, rvp_g)
        elif(category == 'SC'):
            rvp_sc = rvp[rvp['CATEGORY'] == 'SC']
            z = predictor(perc, rvp_sc)
        elif(category == 'ST'):
            rvp_st=rvp[rvp['CATEGORY']=='ST']
            z = predictor(perc, rvp_st)
        elif(category == 'EWS'):
            rvp_e = rvp[rvp['CATEGORY'] == 'EWS']
            z = predictor(perc, rvp_e)
        else:
            rvp_ob = rvp[rvp['CATEGORY'] == 'OBC-NCL']
            z = predictor(perc, rvp_ob)

    k = float(np.round(z))
    if(k <= 0):
        k = 15
    return k

def predictor(perc, rvp):
    X = rvp['PERCENTILE'].values.reshape(-1,1)
    y = rvp['RANK'].values.reshape(-1,1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    x = pd.Series([perc])
    z = regressor.predict(x.values.reshape(-1,1))
    return z
