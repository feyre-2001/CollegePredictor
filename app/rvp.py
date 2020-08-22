def pvr(perc,pwd,category):
    import sklearn;
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

    import csv
    from pathlib import Path

    base_path = Path(__file__).parent
    file_path = (base_path / "..//app//rvp_cleaned.csv").resolve()


    rvp=pd.read_csv(file_path)
    rvp_g=rvp[rvp['CATEGORY']=='GEN']
    rvp_gp=rvp[rvp['CATEGORY']=='GEN-PwD']
    rvp_e=rvp[rvp['CATEGORY']=='EWS']
    rvp_ep=rvp[rvp['CATEGORY']=='EWS-PwD']
    rvp_sc=rvp[rvp['CATEGORY']=='SC']
    rvp_scp=rvp[rvp['CATEGORY']=='SC-PwD']
    rvp_st=rvp[rvp['CATEGORY']=='ST']
    rvp_stp=rvp[rvp['CATEGORY']=='ST-PwD']
    rvp_ob=rvp[rvp['CATEGORY']=='OBC-NCL']
    rvp_obp=rvp[rvp['CATEGORY']=='OBC-NCL-PwD']
    if(pwd=='YES'):
        if(category=='GEN'):
            X=rvp_gp['PERCENTILE'].values.reshape(-1,1)
            y=rvp_gp['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='SC'):
            X=rvp_scp['PERCENTILE'].values.reshape(-1,1)
            y=rvp_scp['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='ST'):
            X=rvp_stp['PERCENTILE'].values.reshape(-1,1)
            y=rvp_stp['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='EWS'):
            X=rvp_ep['PERCENTILE'].values.reshape(-1,1)
            y=rvp_ep['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        else:
            X=rvp_obp['PERCENTILE'].values.reshape(-1,1)
            y=rvp_obp['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
    else:
        if(category=='GEN'):
            X=rvp_g['PERCENTILE'].values.reshape(-1,1)
            y=rvp_g['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='SC'):
            X=rvp_sc['PERCENTILE'].values.reshape(-1,1)
            y=rvp_sc['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='ST'):
            X=rvp_st['PERCENTILE'].values.reshape(-1,1)
            y=rvp_st['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        elif(category=='EWS'):
            X=rvp_e['PERCENTILE'].values.reshape(-1,1)
            y=rvp_e['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
        else:
            X=rvp_ob['PERCENTILE'].values.reshape(-1,1)
            y=rvp_ob['RANK'].values.reshape(-1,1)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            x=pd.Series([perc])
            z=regressor.predict(x.values.reshape(-1,1))
    return float(np.round(z))
