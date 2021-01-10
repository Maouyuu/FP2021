from os import listdir
from os.path import isfile, join
import pandas as pd


"""
    This script merges the two dataframes by LogNumber using MachineId 33 for file 1 and 63 for file 2
"""

PATH = r"C:\Users\Ilyas\Desktop\projetFP\données"
files = [f.split('_Rapp')[0] for f in listdir(PATH) if isfile(join(PATH, f))]
files = files[::2]


def merger(path, name):
    try:
        data1 = pd.read_csv(join(path, name+'_Rapport.csv'))
    except:
        print(join(path, name+'_Rapport.csv') + '\t does not exist')
        return
    try:
        data2 = pd.read_csv(join(path, name+'_Rapport_PGLR.csv'))
    except:
        print(join(path, name+'_Rapport_PGLR.csv') + '\t does not exist')
        return

    clean_data1 = data1.loc[data1["MachineId"] == 33]
    clean_data1 = clean_data1.set_index('LogNumber')

    clean_data2 = data2.loc[data2["MachineId"] == 63][['LogNumber', 'Degrees',
                                                       'TurnDescription', 'DetectedTurnError', 'ClassifiedDetectedTurnError']]
    clean_data2 = clean_data2.set_index('LogNumber')

    data = pd.merge(clean_data1, clean_data2, left_index=True, right_index=True)

    data.to_csv(join(r"C:\Users\Ilyas\Desktop\projetFP\clean-données", name + ".csv"))


for file_name in files:
    merger(PATH, file_name)
