import os
import glob
from pathlib import Path

import json
import csv
import numpy as np
import pandas as pd 
import sklearn as sk 
from sklearn.manifold import TSNE


def tsne_cluster():
    pass

def data_preprocess(df):
    names1  = df["match_id"].astype(str)
    names2  = df["match_id"].astype(str)
    name1 = [name.split('-')[-1] for name in names1]
    name2 = [name.split('-')[-2] for name in names2]
    df['name1'] = name1
    df['name2'] = name2
    print(df.head())

def checksparseness(df):
    sparse = dict()
    sparse["totalrows"] = df.shape[0]

    columns = df.columns.values
    print("columns: ",columns)
    for column in columns:
        columndata = df[column]
        count = int(columndata.isna().sum())
        sparse[column] = count


    return sparse

def cyclesparsenessfiles(dflist,filenames):
    resultdict = dict()
    for [df,filename] in zip(dflist,filenames):
        result = checksparseness(df)
        resultdict[str(filename)] = result
    
    return resultdict

def read_charting_data(directory):
    dflist = []
    filenames = []
    for filepath in Path(directory).glob('**/*'):
        afile = filepath.absolute()
        #print(afile)
        extension = afile.suffix
        #print(extension)
        if(extension ==".csv"):
            print(afile)
            df = pd.read_csv(afile, engine='python',index_col=False) #,error_bad_lines=False) #, quoting=csv.QUOTE_NONE, encoding='utf-8')
            dflist.append(df)
            filenames.append(os.path.basename(afile))
            #if(filenames[-1] == "charting-m-stats-ReturnOutcomes.csv"): #"charting-m-stats-ReturnOutcomes.csv"):
                #print(df)

    return dflist,filenames

def main():
    dirname = Path("/home/dima/Desktop/datamining/project/files/tennis_MatchChartingProject")
    files = os.listdir(dirname)
    #print(files)
    dflist,filenames = read_charting_data(dirname)
    #print(dflist)

    result = cyclesparsenessfiles(dflist,filenames)
    print(result)

    data_preprocess(dflist[4])
    #df = pd.read_csv()
    with open('ChartingProjectSparsity.json', 'w') as outfile:
        json.dump(result,outfile,indent=4)

if __name__ == "__main__":
    main()