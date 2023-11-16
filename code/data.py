import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats


def extract_data(year="2008"):
    year = int(year)
    sets = [f for f in os.listdir("datasets")]
    data = {}
    
    for set in sets:
        data[int(set.removeprefix("interventions").removesuffix(".csv"))] = pd.read_csv("datasets" + os.sep + set, sep=";", index_col=0, encoding='latin-1')

    return data[year].head()

def create_dataset(category="Dataset Column", years=["a","b","..."]):
    new_dataset = {}
    for year in years:
        data = extract_data(year)

    new_my_dict = [
    {'a': 15, 'n': 81, 'p': 177}
    ]
    df = pd.DataFrame.from_dict(new_my_dict) 
    df.to_csv (r'test8.csv', index=False, header=True)


if __name__ == "__main__":
    dataset = extract_data(input())

