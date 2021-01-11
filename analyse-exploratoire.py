from os.path import join
from os import listdir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


PATH = r"C:\Users\Ilyas\Desktop\projetFP\clean-données"
files = [f for f in listdir(PATH)]
data = pd.concat([pd.read_csv(join(PATH, file)) for file in files], ignore_index=True)

nan_cols = ['StemId', 'BinId', 'Crew', 'AcousticVelocity', 'VelocityClass', 'DestinationName']
one_value_cols = ['MachineId', 'SpeciesName', 'IsMetric', 'ForceTerm', 'IsSimulation',
                  'ChipValue', 'SawdustValue', 'NaturalFreq', 'Confidence', 'Harmonic', 'CurveDeflection']
useless_cols = ['RealDateTime', 'UUID']
data.drop(columns=nan_cols + one_value_cols+useless_cols, inplace=True)
data.shape
categorical_variables = ['CutPatternDescription', 'GradeName', 'Shift', 'PieceCount', 'DiameterDescription',
                         'LenghtDescription', 'SolutionType', 'FiberClass', 'EdgerFlitchCount', 'SubWidthBoardCount', 'SweepClass', 'OptTimeClass']
