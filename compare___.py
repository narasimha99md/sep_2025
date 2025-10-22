import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'salary': [1000, 2000, 3000, 4000]
})

df2 = pd.DataFrame({
    'id': [1, 2, 4, 5],
    'name': ['A', 'B1', 'D', 'E'],
    'salary': [1000, 2500, 4000, 5000]
})

cols =['name','salary']
df_merged =df1.merge(df2, on ='id',how='outer',indicator=True,suffixes=('_df1','_df2'))
#print(df_merged)
### Recoreds present only in df1
df_df1_records =df_merged[df_merged['_merge'] =='left_only']
print("df1_only_records:\n",df_df1_records)

### Recoreds present only in df2
df_df2_records =df_merged[df_merged['_merge'] =='right_only']
print("df2_only_records:\n",df_df2_records)

### Recoreds present  in df1 & df2(common records)
df_common_records =df_merged[df_merged['_merge'] =='both']
print("common_records:\n",df_common_records)

### Mismatch Recoreds from df1 & df2(common records)
df_mismatch = df_common_records[
    (df_common_records[[c+'_df1' for c in cols]].values != df_common_records[[c+'_df2' for c in cols]].values ).any(axis=1)
    ]

print("Mismatched Recs: \n",df_mismatch)
#### Combine all mismatched
df_all_mismatches = pd.concat([df_df1_records,df_df2_records,df_mismatch])
print("All mismatched \n",df_all_mismatches)

# 🔹 Write to CSV
df_all_mismatches.to_csv("final_mismatches.csv", index=False)
