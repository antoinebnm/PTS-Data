# Imports
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#
# Path in .py file is :
#       PATH = "datasets" + os.sep
#
# Path in .ipynb file is :
#       PATH = ".." + os.sep + "datasets" + os.sep
#
PATH = "datasets" + os.sep


# Functions
def load_dataset(name=str, path=PATH) -> pd.DataFrame:
    # load csv dataset from local folders (indicate path and file name)
    data = pd.read_csv(path + name, sep=";", encoding='utf-8')

    return data     # Return a DataFrame

def create_dataset(category="Dataset Column (Category)", arg="Dataset Row (Value)", datasets=[".csv"], path=PATH) -> None:
    new_dataset = []
    # List, load, search into datasets
    for name in datasets:
        row = []
        data = load_dataset(name, path)

        if new_dataset == []:
            for col in data.columns:
                row.append(col)
            new_dataset.append(row)

        for i,x in enumerate(data[category]):
            if x == arg:
                row = []
                for y in data.iloc[i]:
                    row.append(y)
                new_dataset.append(row)

    df = pd.DataFrame.from_dict(new_dataset)
    df.to_csv(PATH + f'{category.capitalize()}' + os.sep + rf'{arg.lower()}.csv', index=False, header=False, sep=';')

def clear_df(set, path) -> None:
    data = load_dataset(set, path)
    new_dataset = []
    row = []

    if new_dataset == []:
        for col in data.columns:
            row.append(col)
        new_dataset.append(row)

    for x in data.index:
        row = []
        for y in data.iloc[x]:
            try:
                y = np.int64(y)
            except:
                try:
                    if int(str(y)[0]) <= 9:
                        y = np.int64(''.join(y.split(' ')))
                except:
                    pass
            if y == -9223372036854775808:
                y = np.nan
            row.append(y)
        new_dataset.append(row)
    """
    df = pd.DataFrame.from_dict(new_dataset)
    df.to_csv(PATH + os.sep + rf'{set.lower()}', index=False, header=False, sep=';')"""

if __name__ == "__main__":
    datasets = [f for f in os.listdir(PATH)]
    for set in datasets:
        dataset = load_dataset(name=set)
        break