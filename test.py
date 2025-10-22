from unittest.mock import inplace

import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['A', 'B', 'C', 'D', 'E'],
    'dept': ['HR', 'IT', 'HR', 'IT', 'Sales'],
    'salary': [3000, 4000, 3500, np.nan, 5000]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'bonus': [300, 400, 350, 200, 500]
})

print("Original DataFrame:")
print(df1)

# -------------------------------
# 2️⃣ Handle missing values
# -------------------------------
print("After fillna DataFrame:")
df1['salary']= df1['salary'].fillna(df1['salary'].mean())
print(df1)