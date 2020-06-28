import pandas as pd 
import numpy as np 
import os
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 
import json

def loaddata(filename):
    df = pd.read_csv(filename)
    return df

def subsampledata(df,col):
    df = df[col]
    df.dropna(inplace = True)
    return df

def histogram(data,savefile):
    plt.hist(data)
    plt.savefig(savefile+'png')
    plt.close()

def countNaNs(df):
    dictionary = {}
    columns = df.head()
    for col in columns:
        data = df[col]
        count = data.isna().sum()
        dictionary[col] = count
    return dictionary

def savedatainfile(dictionary,filename):
    for key in dictionary.keys():
        dictionary[key] = (int)(dictionary[key])

    with open(filename, 'w') as fp:
        json.dump(dictionary, fp,indent=4)


if __name__ == "__main__":
    filename = 'files/datahub/player_overviews.csv'
    #['height_cm','handedness','backhand']
    df = loaddata(filename)
    length = df.shape[0]
    print(length)

    dict_players = countNaNs(df)
    savedatainfile(dict_players,'player_data.json')


    #sample = subsampledata(df,['height_cm','handedness','backhand'])
    # sample1 = subsampledata(df,'handedness')
    # sample2 = subsampledata(df,'backhand')
    # print(type(df),type(sample1))
    # histogram(sample1,'handedness')
    # histogram(sample2,'backhand')
    #print(df)

