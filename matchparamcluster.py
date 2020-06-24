import pandas as pd 
import numpy as np 
import os
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 

def loaddata(filename):
    print(filename)
    df = pd.read_csv(filename)
    return df

def subsampledata(df,col):
    df = df[col]
    df.dropna(inplace = True)
    return df

def mergedataframes(dflist):
    result = pd.concat(dflist)
    return result


def histogram(data,savefile):
    plt.hist(data)
    plt.savefig(savefile+'.png')
    plt.close()

if __name__ == "__main__":
    dirname = 'files/jeffsackmanndata'
    files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
    #['height_cm','handedness','backhand']
    files.remove('README.md')
    files.remove('matches_data_dictionary.txt')
    files.remove('atp_players.csv')
    files.remove('atp_rankings_current.csv')
    files.remove('atp_rankings_90s.csv')
    files.remove('atp_rankings_80s.csv')
    files.remove('atp_rankings_70s.csv')
    files.remove('atp_rankings_10s.csv')
    files.remove('atp_rankings_00s.csv')
    #print(files)
    dflist = [loaddata(os.path.join(dirname,f)) for f in files if os.path.isfile(os.path.join(dirname,f))]
    print(len(dflist))
    df = mergedataframes(dflist)
    print(dflist[0].shape,df.shape)
    df.to_csv('test.csv')
    # df = loaddata(files[0])
    # length = df.shape[0]
    # print(length)


    # sample = subsampledata(df,['height_cm','handedness','backhand'])
    # sample1 = subsampledata(df,'handedness')
    # sample2 = subsampledata(df,'backhand')
    # print(type(df),type(sample1))
    # histogram(sample1,'handedness')
    # histogram(sample2,'backhand')
    #print(df)

