import pandas as pd 
import numpy as np 
import os
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 
import pickle
import json

def loaddata(filename):
    #print(filename)
    df = pd.read_csv(filename,header=0)
    return df

def mergedataframes(dflist):
    first = dflist[0]
    others = dflist[1:-1]
    result = first.append(others, ignore_index=True, sort=False) #,axis=0, join='outer', ignore_index=False, keys=None,
          #levels=None, names=None, verify_integrity=False, copy=True)
    return result

def savedatainfile(csv,filename):
    with open(filename, 'w') as f:
        print(csv,file=f)

def countNaNs(df):
    dictionary = {}
    columns = df.head()
    for col in columns:
        data = df[col]
        count = data.isna().sum()
        dictionary[col] = count
    return dictionary

def loadjacksackmann():
    dirname = 'files/jeffsackmanndata'
    files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
    files.remove('README.md')
    files.remove('matches_data_dictionary.txt')
    files.remove('atp_players.csv')
    files.remove('atp_rankings_current.csv')
    files.remove('atp_rankings_90s.csv')
    files.remove('atp_rankings_80s.csv')
    files.remove('atp_rankings_70s.csv')
    files.remove('atp_rankings_10s.csv')
    files.remove('atp_rankings_00s.csv')
    files_singles = [f for f in files if (f.find('double')==-1)]
    files_doubles = [f for f in files if (f.find('double')!=-1 and f.find('future')==-1)]
    print(files_singles)
    print('test: ',len(files),len(files_doubles),len(files_singles))
    dflist_singles = [loaddata(os.path.join(dirname,f)) for f in files_singles if os.path.isfile(os.path.join(dirname,f))]
    dflist_doubles = [loaddata(os.path.join(dirname,f)) for f in files_doubles if os.path.isfile(os.path.join(dirname,f))]
    df_singles = mergedataframes(dflist_singles)
    df_doubles = mergedataframes(dflist_doubles)

    return df_singles

def augmentheightdata(addto,addedfrom):
    addedfrom = addedfrom[['First','','']]
    addto = addto[['winner_name','winner_ht']]

if __name__ == "__main__":
    filename = 'files/datahub/player_overviews.csv'
    df1 = loaddata(filename)
    df2 = loadjacksackmann() 
    augmentheightdata(df1,df2)
    #length = df1.shape[0]
    #print(length)

    #dict_players = countNaNs(df1)
    #savedatainfile(dict_players,'player_data.txt')