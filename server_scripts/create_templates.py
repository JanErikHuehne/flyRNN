import pandas as pd
import numpy as np 
import pickle 

with open('../data/pan_neuronal_meta.pkl', 'rb') as f:
    meta_data = pickle.load(f)

for index, k in meta_data.iterrows():
    filepath = ""