from os.path import join
from os import listdir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

"""
    This file is for exploration and testing purposes
"""

PATH = "C:\\Users\\Ilyas\\Desktop\\projetFP\\données\\"

# Data importation
data1 = pd.read_csv(PATH+'2020-12-01_jour_Rapport.csv')
data1

data2 = pd.read_csv(PATH+'2020-12-01_jour_Rapport_PGLR.csv')
data2

# Colonnes communes
keys = list(set(data1.columns) & set(data2.columns))
keys

# Détecter si LogNumber est unique
data1.LogNumber.value_counts()

# Mettre le LogNumber comme index
clean_data1 = data1.loc[data1["MachineId"] == 33]
clean_data1 = clean_data1.set_index('LogNumber')
clean_data1

clean_data2 = data2.loc[data2["MachineId"] == 63][['LogNumber', 'Degrees',
                                                   'TurnDescription', 'DetectedTurnError', 'ClassifiedDetectedTurnError']]
clean_data2 = clean_data2.set_index('LogNumber')
clean_data2

data = pd.merge(clean_data1, clean_data2, left_index=True, right_index=True)
data

data.shape

data.to_csv("C:\\Users\\Ilyas\\Desktop\\projetFP\\clean-données\\" + "2020-12-01_jour.csv")


# Consolider toutes les bases de données
PATH2 = r"C:\Users\Ilyas\Desktop\projetFP\clean-données"
files = [f for f in listdir(PATH2)]
data = pd.concat([pd.read_csv(join(PATH2, file)) for file in files], ignore_index=True)
data.shape

# variables
nan_cols = ['StemId', 'BinId', 'Crew', 'AcousticVelocity', 'VelocityClass', 'DestinationName']
data.drop(columns=nan_cols, inplace=True)
vars = data.columns
for var in vars:
    print(var + '\t' + str(len(set(data[var]))))
one_value_cols = ['MachineId', 'SpeciesName', 'IsMetric', 'ForceTerm', 'IsSimulation',
                  'ChipValue', 'SawdustValue', 'NaturalFreq', 'Confidence', 'Harmonic', 'CurveDeflection']

# Data Cleaning
PATH2 = r"C:\Users\Ilyas\Desktop\projetFP\clean-données"
files = [f for f in listdir(PATH2)]
data = pd.concat([pd.read_csv(join(PATH2, file)) for file in files], ignore_index=True)
data.drop(columns=nan_cols + one_value_cols, inplace=True)

# TO DO
# Analyse explorative des données
