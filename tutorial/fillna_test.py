import pandas as pd
import numpy as np

# データを作成
data = {'列1': [1, np.nan, 3], '列2': [4, 5, np.nan], '列3': [7, 8, 9]}
df = pd.DataFrame(data)
li = list(df.columns)
print(li)
# 全ての列を0で埋める

df[li] = df[li].fillna(0)
# df.fillna(0, inplace=True)

# 結果を表示
print(df)