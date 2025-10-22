import pandas as pd

df1 = pd.DataFrame({
    "id":[1,2,3,4],"name":['A','B','C','D'],"salary":[2000,3500,5600,2400]
})

df2 = pd.DataFrame({
    "id":[1,2,3,5],"name":['A1','B','C','D'],"salary":[2000,3500,5000,2400]
})


cols = ['name','salary']

df_merged = df1.merge(df2, on ='id', how='outer', indicator=True,suffixes=('_df1','_df2'))
'''#print(df_merged_src_tgt)'''


common = df_merged[df_merged['_merge'] == 'both']
print("common \n",common)

mismatched = common[
    (common[[c + '_df1' for c in cols]].values != common[[c + '_df2' for c in cols]].values).any(axis=1)
]