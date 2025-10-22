import pandas as pd
import datacompy

# Create two sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'salary': [1000, 2000, 3000, 4000]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'X', 'D'],
    'salary': [1000, 2500, 3000, 4000]
})

compare = datacompy.Compare(
    df1,
    df2,
    join_columns=['id'],   # Common key(s) to join on
    df1_name='Source',
    df2_name='Target'
)

print(compare.report())
