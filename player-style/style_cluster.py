import os
import glob
from pathlib import Path

import csv
import numpy as np
import pandas as pd 
import sklearn as sk 
from sklearn.manifold import TSNE


def tsne_cluster():
    pass

def data_preprocess():
    pass

def read_charting_data(directory):
    dflist = []
    for filepath in Path(directory).glob('**/*'):
        afile = filepath.absolute()
        print(afile)
        extension = afile.suffix
        print(extension)
        if(extension ==".csv"):
            df = pd.read_csv(afile, error_bad_lines=False, engine='python') #, quoting=csv.QUOTE_NONE, encoding='utf-8')
            dflist.append(df)

    return dflist

def main():
    dirname = Path("/home/dima/Desktop/datamining/project/files/tennis_MatchChartingProject")
    files = os.listdir(dirname)
    #print(files)
    dflist = read_charting_data(dirname)
    print(dflist)
    #df = pd.read_csv()

if __name__ == "__main__":
    main()