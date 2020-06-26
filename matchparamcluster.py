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

    #with open(filename, 'w') as f:
    # print(dictionary,file=f)

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
    files_singles = [f for f in files if (f.find('double')==-1)]
    files_doubles = [f for f in files if (f.find('double')!=-1 and f.find('future')==-1)]
    print(files_singles)
    print('test: ',len(files),len(files_doubles),len(files_singles))
    dflist_singles = [loaddata(os.path.join(dirname,f)) for f in files_singles if os.path.isfile(os.path.join(dirname,f))]
    dflist_doubles = [loaddata(os.path.join(dirname,f)) for f in files_doubles if os.path.isfile(os.path.join(dirname,f))]

    #print(len(dflist_singles))
    df_singles = mergedataframes(dflist_singles)
    df_doubles = mergedataframes(dflist_doubles)
    print(dflist_singles[0].shape,df_singles.shape)
    dict_singles = countNaNs(df_singles)
    print('NaN rows count: ',dict_singles)
    dict_doubles = countNaNs(df_doubles)
    print('NaN double count: ', dict_doubles)

    savedatainfile(dict_singles,'singles_sparsity.json')
    savedatainfile(dict_doubles,'doubles_sparsity.json')




    #df_doubles.to_csv('test.csv')
    # df = loaddata(files[0])
    # length = df.shape[0]
    # print(length)
    #[print(f.shape) for f in dflist_doubles]



#https://stackoverflow.com/questions/28199524/best-way-to-count-the-number-of-rows-with-missing-values-in-a-pandas-dataframe
#https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file
#https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes (pickle issue)

# what are the issues:
# - singles and doubles different
#   - need to have both entries
# - need to get empty rows per column
# - need to write results to file