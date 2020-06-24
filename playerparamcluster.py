import pandas as pd 
import numpy as np 
import os
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 

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

if __name__ == "__main__":
    filename1 = 'files/datahub/player_overviews.csv'
    filename2 = 'files/'
    #['height_cm','handedness','backhand']
    df = loaddata(filename1)
    length = df.shape[0]
    print(length)


    #sample = subsampledata(df,['height_cm','handedness','backhand'])
    sample1 = subsampledata(df,'handedness')
    sample2 = subsampledata(df,'backhand')
    print(type(df),type(sample1))
    histogram(sample1,'handedness')
    histogram(sample2,'backhand')
    #print(df)

