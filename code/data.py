import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats


def extract_data(year=2008):
    sets = [f for f in os.listdir("datasets")]
    data = {}
    
    for set in sets:
        data[int(set.removeprefix("interventions").removesuffix(".csv"))] = pd.read_csv("datasets" + os.sep + set, sep=";", index_col=0, encoding='latin-1')
    
#    INDEX = str(input("Année (de 2008 à 2021) : "))
#    print(data[INDEX].head())
    return data[year].head()
