import pandas as pd 
import numpy as np 
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 

def loaddata(filename):
    df = pd.read_csv(filename)
    return df

def subsampledata(df):
    df = df[['height_cm','handedness','backhand']]
    df.dropna(inplace = True)
    return df

def histogram(data):
    plt.hist(data)
    plt.show()

if __name__ == "__main__":
    filename = 'files/datahub/player_overviews.csv'
    
    df = loaddata(filename)
    df = subsampledata(df)
    histogram(df['handedness'])
    histogram(df['backhand'])
    print(df)

