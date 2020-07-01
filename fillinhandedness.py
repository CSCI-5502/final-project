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

def savedatainfile(df,filename):
    df.to_csv(filename)

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

def transform_name(first,last):
    #print(first,"::",last)
    first = str(first)
    last = str(last)
    first = first.lower()
    last = last.lower()
    name = first+'-'+last
    return name

def fetchdatahubplayer(df,name):
    row = df.loc[df['player_slug'] == name]
    #print(name, '\nRow: ', row)
    return row


def augmenthandednessdata(addto,addedfrom):
    #addedfrom = addedfrom[[2,3,4]]

    total = addedfrom.shape[0]
    for idx,row in addedfrom.iterrows(): 
        #print(row)
        
        #print("name: ",row[1] , ':', row[2])
        name = transform_name(row[1],row[2])
        #print('name: ',name)
        query = fetchdatahubplayer(addto,name)
        #print('name:', name ,'test: ',query.index)
        if(len(query.index) > 0 ):
            addidx = query.index[0]
            entry = row[3]
            #print('query: ',query,'entry:',entry)
            datum = ''
            if(entry == 'R'):
                datum = 'Right-Handed'
            if(entry == 'L'):
                datum = 'Left-Handed'
            if(entry == 'U'):
                datum = 'Ambidextrous'
            addto['handedness'][addidx] = datum
        if(idx% 100 == 0):
            print('step: ',idx , ":",total)

        

    return addto

def transform_name2(name):
    name = str(name)
    name = name.lower()
    name = name.replace(' ','-')
    return name

def augmentheightdata(addto,addedfrom):
    total = addedfrom.shape[0]
    print(total)
    for idx,row in addedfrom.iterrows(): 
        #print(row)
        #print("name: ",row[10])
        name = transform_name2(row[10])
        #print('name: ',name)
        query = fetchdatahubplayer(addto,name)
        #print('name:', name ,'test: ',query.index)
        if(len(query.index) > 0 ):
            addidx = query.index[0]
            entry = row[12]
            #print('query: ',query,'entry:',entry)
            addto['height_cm'][addidx] = entry
        if(idx% 100 == 0):
            print('step: ',idx , ":",total)
    return addto

if __name__ == "__main__":
    filename1 = 'files/datahub/player_overviews.csv'
    filename2 = 'files/jeffsackmanndata/atp_players.csv'
    df1 = loaddata(filename1)
    df2 = loaddata(filename2) 
    df3 = loadjacksackmann()
    #print(df1.head())
    #print(df2.head())    
    result = augmenthandednessdata(df1,df2)
    result = augmentheightdata(result,df3)
    print(result.head())
    #length = df1.shape[0]
    #print(length)

    #dict_players = countNaNs(df1)
    savedatainfile(result,'augmented_player_overview.csv')