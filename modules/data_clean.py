import pandas as pd
import numpy as np


def perc_null(X):
    
    total = X.isnull().sum().sort_values(ascending=False)
    data_types = X.dtypes
    percent = (X.isnull().sum()/X.isnull().count()).sort_values(ascending=False)

    missing_data = pd.concat([total, data_types, percent], axis=1, keys=['Total','Type' ,'Percent'])
    return missing_data

#for X in data_frames:
#    print(perc_null(X)['Total'].sum())

##goalie stats, skater stats, team_stats all have NaN ... 
## I think missing vals are in df_mp ... deal later