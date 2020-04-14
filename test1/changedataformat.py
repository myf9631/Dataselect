import numpy as np
import pandas as pd

data = np.load('data10.npy')
df_data = pd.DataFrame(data)
df_data.to_csv('data10.csv')

data = np.load('data11.npy')
df_data = pd.DataFrame(data)
df_data.to_csv('data11.csv')
