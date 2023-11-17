# Imports
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

interventions = [f for f in os.listdir("datasets" + os.sep + "Interventions")]

# Functions
def load_dataset(name=str, path=str) -> pd.DataFrame:
    # load csv dataset from local folders (indicate path and file name)
    data = pd.read_csv("datasets" + os.sep + path + os.sep + name, sep=";", encoding='latin-1')

    return data

def create_dataset(category="Dataset Column (Category)", arg="Dataset Row (Value)", datasets=["interventions2008"], path="Interventions") -> None:
    if not os.path.exists('datasets' + os.sep + category):
        os.makedirs('datasets' + os.sep + category)

    new_dataset = []
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
    df.to_csv('datasets' + os.sep + f'{category.capitalize()}' + os.sep + rf'{arg.lower()}.csv', index=False, header=False, sep=';')


if __name__ == "__main__":
    create_dataset(category="Département", arg="Paris", datasets=interventions, path="Interventions")
