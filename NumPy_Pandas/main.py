import numpy as np
import pandas as pd

nme = ['Jack', 'Cami', 'Amy', 'Callum', 'Nikole']
age = [29, 30, 28, 28, 25]
deg = ['Chemistry', 'Marine Biology', 'History', 'Marine Biology', 'Psychology']

example_dict = {'name': nme, 'degree': deg, 'score': age}

series_dict = pd.Series(example_dict, index=['degree', 'age', 'name'])
ser_list = pd.Series(deg, index=nme)

print(ser_list)
