#- * - coding: gb2312 -*-
import numpy as  np
import  pandas as  pd

data_df1 = np.load('20181107-20190228.npy')

print(data_df1.shape) # (3224,35)
#np.delete[data_df2]
print(data_df1)

data_df2 = pd.DataFrame(data_df1)
print(data_df2)
data_df2.to_csv('20181107-20190228.csv')





















