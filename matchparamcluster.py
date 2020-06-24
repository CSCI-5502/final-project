import pandas as pd 
import numpy as np 
import os
from sklearn.manifold import TSNE 
import matplotlib.pyplot as plt 

def loaddata(filename):
    #print(filename)
    df = pd.read_csv(filename,header=0)
    return df

def subsampledata(df,col):
    df = df[col]
    df.dropna(inplace = True)
    return df

def mergedataframes(dflist):
    first = dflist[0]
    others = dflist[1:-1]
    result = first.append(others, ignore_index=True, sort=False) #,axis=0, join='outer', ignore_index=False, keys=None,
          #levels=None, names=None, verify_integrity=False, copy=True)
    return result


def histogram(data,savefile):
    plt.hist(data)
    plt.savefig(savefile+'.png')
    plt.close()

def countrowswithNaN(df):
    return sum([True for idx,row in df.iterrows() if any(row.isnull())])

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
    files_singles = [f for f in files if (f.find('double')==-1 and f.find('future')!=-1)]
    files_doubles = [f for f in files if (f.find('double')!=-1 and f.find('future')==-1)]
    print(files_doubles)
    print('test: ',len(files),len(files_doubles),len(files_singles))
    dflist_singles = [loaddata(os.path.join(dirname,f)) for f in files_singles if os.path.isfile(os.path.join(dirname,f))]
    dflist_doubles = [loaddata(os.path.join(dirname,f)) for f in files_doubles if os.path.isfile(os.path.join(dirname,f))]

    #print(len(dflist_singles))
    df_singles = mergedataframes(dflist_singles)
    df_doubles = mergedataframes(dflist_doubles)
    print(dflist_doubles[0],df_doubles)
    count = countrowswithNaN(df_doubles)
    print('NaN rows count: ',count)
    df_doubles.to_csv('test.csv')
    # df = loaddata(files[0])
    # length = df.shape[0]
    # print(length)
    [print(f.shape) for f in dflist_doubles]

    # sample = subsampledata(df,['height_cm','handedness','backhand'])
    # sample1 = subsampledata(df,'handedness')
    # sample2 = subsampledata(df,'backhand')
    # print(type(df),type(sample1))
    # histogram(sample1,'handedness')
    # histogram(sample2,'backhand')
    #print(df)



#https://stackoverflow.com/questions/28199524/best-way-to-count-the-number-of-rows-with-missing-values-in-a-pandas-dataframe