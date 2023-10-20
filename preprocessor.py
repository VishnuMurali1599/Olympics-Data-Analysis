import pandas as pd

df=pd.read_csv("athlete_events.csv")
region_df=pd.read_csv('noc_regions.csv')

def preprocess(df,region_df):
    
    #Filtering For Summer Olympics
    df  = df[df['Season']=='Summer']
    
    #Merge With Region_df
    df=df.merge(region_df,on='NOC',how="left")
    
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    
    #One Hot Encoding
    df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    
    return df