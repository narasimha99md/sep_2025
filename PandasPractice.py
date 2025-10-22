import numpy as np
import pandas as pd
'''
# Read all the rows and columns
# SQL: select * from emp
df = pd.read_csv("emp.csv")
print(df)

#select eno,salary from file
# SQL : select eno,salary from emp
df1 = pd.read_csv("emp.csv",usecols=['eno','salary'])
print(df1)



#read single from file
df1 = pd.read_csv("emp.csv")
data=df1['eno']
print(df1['eno']) # data displays without column name
print(type(data))#<class 'pandas.core.series.Series'>

#read multiple single from file
df1 = pd.read_csv("emp.csv")
print(df1[['eno','ename','salary']])# data display with column names


## find data type of DataFrame fields
df1 = pd.read_csv("emp.csv")
print(df1.dtypes)

## convert doj field data type from object to date
df1 = pd.read_csv("emp.csv",parse_dates=['doj'])
print(df1.dtypes)

## extract yer/month/day part from date
df1 = pd.read_csv("emp.csv",parse_dates=['doj'])
print(df1.dtypes)
print(df1)
print(df1['doj'].dt.year) # year part
print(df1['doj'].dt.month) #month part
print(df1['doj'].dt.day) # day part

## convert data type  from file while reading --
df1 = pd.read_csv("emp.csv")
print(df1.dtypes)
print(df1)

df1 = pd.read_csv("emp.csv",parse_dates=['doj'],dtype={'salary':float})
print(df1.dtypes)
print(df1)

####
import pandas as pd

# Suppose you already loaded your DataFrame
df1 = pd.read_csv("emp.csv")

# View current data types
print("Before conversion:")
print(df1.dtypes)

df1["salary"] = df1["salary"].astype(float)
df1["emp_id"] = df1["eno"].astype(int)
df1["ename"] = df1["ename"].astype(str)
df1["doj"] = pd.to_datetime(df1["doj"])

#Convert multiple columns at once
import pandas as pd

df1 = pd.read_csv("emp.csv")
# Convert salary and emp_id first
df1 = df1.astype({
    "salary": "float",
    "eno": "int",
    "ename": "str"

})

print(df1.dtypes)


# read specific row

import pandas as pd

df1 = pd.read_csv("emp.csv")
print(df1)
#print(df1.iloc[1]) #single row data
print(df1.iloc[0:5]) #5 rows of data , 0,1,2,3,4
print(df1.iloc[0:5:1]) #5 rows of data , 0,1,2,3,4
print(df1.iloc[0:5:2]) #3 rows of data , 0,2,4

# read 5th to 9 rows
print(df1.iloc[5:10:1]) #5 rows from 5th to 9th row

#way2 read 5th to 9 rows
df1 = pd.read_csv("emp.csv",skiprows=5,nrows=5)
print(df1) #5 rows from 5th to 9th row

#way2 read 5th to 9 rows and rname the header
df1 = pd.read_csv("emp.csv",skiprows=5,nrows=5,names=['empno','ename','salary','deptno','doj'])
print(df1) #5 rows from 5th to 9th row


###another way
df1 = pd.read_csv("emp.csv",header=10)
print(df1)



## Reading cvs file when delimiter is ';'

df1 = pd.read_csv("emp1.csv",delimiter=';')
print(df1)


#### performance



import pandas as pd

for chunk in pd.read_csv("emp1.csv", chunksize=5, on_bad_lines='skip'):
    print(chunk)
    

####
for chunk in pd.read_csv("emp.csv", chunksize=5):
    print(chunk)


##
df = pd.read_csv("emp.csv", low_memory=True)
print(df)
# Note: to avoid any data curruption set low_memory=False
print(df.head(4))
print(df.tail(2))


###############June barch Pandas- Day-1 video
# Way 1: fecth 10th record from DataFrame

df = pd.read_csv("emp.csv")
df10 =df.head(10)
print(df10.tail(1))


# Way 2: fecth 10th record from DataFrame
df = pd.read_csv("emp.csv")
print(df.head(10).tail(1))



# Way 2: Desc table
df = pd.read_csv("emp.csv")
print(df.info())
# Way 2: columns in df
print(df.columns) #Index(['eno', 'ename', 'salary', 'deptno', 'doj'], dtype='object')
# Data types
print(df.dtypes)


## read 5 records and wirite in to csv

df = pd.read_csv("emp.csv")
df_res =df.iloc[0:5:2]

df_res.to_csv("emp_results.csv",index=False)# without index
df_res.to_csv("emp_results1.csv") # index also stores in file
# read 2 fields from df
print(df[['eno','ename']])
'''

###############June barch Pandas- Day-2 video --order by & group ,concat,merge by 12th Oct 2025
# Order by - arranging data ascending /descending order
# Group by - grouping row level data into summary level data
# Merge - similar to SQl joins(inner,left,right,outer)
# concat - Appending dataframe on top of another data frame or side by side -similar to Union / cross join
'''
df.head()      # show first 5 rows from top
df.tail()      # show first 5 rows from bottom
df.info()      # show column types and count
df.shape       # show (rows, columns)



df = pd.read_csv(".../../Data/emp.csv")
#print(df)

#print(df.head() )     # show first 5 rows from top
#print(df.tail())      # show first 5 rows from bottom
#print(df.info())      # show column types and count
#print("rows & Coulmns: ",df.shape)       # show (rows, columns)
#df_sort_asc=df.sort_values(by='salary')
#print(df_sort_asc)

#df_sort_desc=df.sort_values(by='salary',ascending=False)
#print(df_sort_desc)

#### Sort 'deptno' ascending and 'salary' descending
#df_sort=df.sort_values(by=['deptno','salary'],ascending=[True,False])
#print(df_sort)

#### Sort 'deptno' ascending and 'salary' descending and save chnages in same dataframe

df.sort_values(by=['deptno','salary'],ascending=[True,False],inplace=True)
print(df)

### convert dictionary to DataFrame
data ={"empid":[1,2,3],"ename":['A','B','C']}
df = pd.DataFrame(data)
print(df)


######## Group buy

df = pd.read_csv(".../../Data/emp.csv")
print(df)
df_group = df.groupby('deptno')['eno'].count()
print(df_group)



df = pd.read_csv(".../../Data/emp.csv")
#print(df)
print( df.groupby('deptno')['eno'].count())
df_group = df.groupby('deptno')['eno'].count().reset_index()
print(df_group)
print(type(df_group))

x= df_group.rename(columns={'eno':'count'})
print(x)


### min, max ,cum, count of salary column department wise

df = pd.read_csv(".../../Data/emp.csv")
print(df)

df_agg=df.groupby('deptno')['salary'].agg(['sum','min','max','count'])
print(df_agg)

print(df.count())  # column wise count

count = len(df)
print("count in DF: ",count)
print(type(count))

count = df.shape[0] ###row count
print(count)

count = df.shape[1] # column count
print(count)



### Group by multiple columns ---- min, max ,cum, count of salary column department wise

df = pd.read_csv(".../../Data/emp.csv")
print(df)

df_agg=df.groupby(['deptno','salary'])['eno'].agg(['count']).reset_index()
print(df_agg)



## Where clause in df
df = pd.read_csv(".../../Data/emp.csv")
print(df)
filter=df['deptno'] ==10
print(filter)

print(df[filter])

###way 2
df = pd.read_csv(".../../Data/emp.csv")
print(df)
filter = df['deptno'].isin([10, 20, 30])
print(df[filter])

###way 3

df = pd.read_csv(".../../Data/emp.csv")
#print(df)

filter = ((df['deptno'] == 10) | (df['deptno'] == 20) | (df['deptno'] == 30)) & (df['salary'] >=2000)
print(df[filter])



## Merge  (joins)  

df_emp = pd.read_csv(".../../Data/emp_name.csv")
#print(df_emp)
df_sal = pd.read_csv(".../../Data/emp_sal.csv")
#print(df_sal)

#df_merge = df_emp.merge(df_sal,on=['eno'] ,how='inner')
#df_merge = df_emp.merge(df_sal,on=['eno'] ,how='left')
#df_merge = df_emp.merge(df_sal,on=['eno'] ,how='right')
df_merge = df_emp.merge(df_sal,on=['eno'] ,how='outer',indicator=True)
print(df_merge)


## Merge  (joins)   when join column name is diff

df_emp = pd.read_csv(".../../Data/emp_name_1.csv")
#print(df_emp)
df_sal = pd.read_csv(".../../Data/emp_sal_1.csv")
#print(df_sal)

#df_merge = df_emp.merge(df_sal,left_on=['eno'],right_on=['empno'] ,how='inner')
#df_merge = df_emp.merge(df_sal,left_on=['eno'],right_on=['empno'],how='left')
#df_merge = df_emp.merge(df_sal,left_on=['eno'],right_on=['empno'] ,how='right')
df_merge = df_emp.merge(df_sal, left_on=['eno'],right_on=['empno'] ,how='outer',indicator=True)
#print(df_merge)

left_only = df_merge[df_merge['_merge'] == 'left_only']
print("Records only in emp file:\n", left_only)

right_only = df_merge[df_merge['_merge'] == 'right_only']
print("Records only in salary file:\n", right_only)

'''
### concat
'''
dict1 ={"empid":[1,2,3],"deptno":[10,20,30]}
dict2 ={"empid":[1,4,5],"deptno":[10,20,30]}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
#print(df2)
##keeps data of d2 under df1
#df_concat = pd.concat([df1,df2])
df_concat = pd.concat([df1,df2],axis=0)
print(df_concat)

##keeps data of d1 and df2 side by side
df_concat1 = pd.concat([df1,df2],axis=1)
print(df_concat1)



import pandas as pd
dict1 ={"eno":[1,2,3],"name":['A', 'B','C']}
dict2 ={"eno":[1,2,4],"name":['A1','B','D']}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
#print(df1)

df_merge = df1.merge(df2,on='eno',how='outer',indicator=True)
print(df_merge)
print("=============")
left_only = df_merge[df_merge['_merge']== 'left_only']
print(left_only)

print("=============")

###########

import pandas as pd


def compare_dataframes(df1, df2, key_columns, output_file="mismatches.csv"):
    """
    Compare two DataFrames and write mismatched records to CSV.

    :param df1: First dataframe (expected data)
    :param df2: Second dataframe (actual data)
    :param key_columns: List of column(s) to join on (like primary key)
    :param output_file: File path to save mismatches
    """

    # Merge dataframes on key columns
    df_merged = df1.merge(df2, on=key_columns, how="outer", indicator=True, suffixes=("_expected", "_actual"))

    # Records present only in one side OR mismatched values
    mismatches = df_merged[df_merged["_merge"] != "both"]

    # Save mismatches to CSV
    mismatches.to_csv(output_file, index=False)
    print(f"✅ Mismatches written to {output_file}")

    return mismatches


# 🔹 Example Usage
df_expected = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40]
})

df_actual = pd.DataFrame({
    "id": [1, 2, 3, 5],
    "name": ["Alice1", "Bobby", "Charlie", "Daniel"],
    "age": [25, 32, 35, 50]
})

mismatches = compare_dataframes(df_expected, df_actual, key_columns=["id"])
print(mismatches)

###############


import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'salary': [1000, 2000, 3000, 4000]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B1', 'C', 'D2'],
    'salary': [1000, 2500, 3000, 4000]
})

# Merge both DataFrames on 'id'
df_merge = df1.merge(df2, on='id', how='outer', suffixes=('_df1', '_df2'), indicator=True)

# Columns to compare
cols = ['name', 'salary']

# Find mismatches (where values differ)
mismatches = df_merge[
    (df_merge[[c + '_df1' for c in cols]].values != df_merge[[c + '_df2' for c in cols]].values).any(axis=1)
]

print("🔹 Mismatched Records:")
print(mismatches)

# Write mismatched data to CSV
mismatches.to_csv('mismatched_records.csv', index=False)
print("\n✅ Mismatched records written to 'mismatched_records.csv'")
'''

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

# 🔹 Merge both dataframes
df_merge = pd.merge(df1, df2, on='id', how='outer', suffixes=('_df1', '_df2'), indicator=True)

# 🔹 Identify missing and mismatched
missing_in_df2 = df_merge[df_merge['_merge'] == 'left_only']
missing_in_df1 = df_merge[df_merge['_merge'] == 'right_only']

# 🔹 Identify mismatched rows (present in both but values differ)
common = df_merge[df_merge['_merge'] == 'both']
cols = ['name', 'salary']
mismatched = common[
    (common[[c + '_df1' for c in cols]].values != common[[c + '_df2' for c in cols]].values).any(axis=1)
]

# 🔹 Combine all mismatches
final_mismatches = pd.concat([missing_in_df1, missing_in_df2, mismatched], ignore_index=True)

# 🔹 Write to CSV
final_mismatches.to_csv("final_mismatches.csv", index=False)

# 🔹 Print summary
print("✅ Mismatch Details:")
print(final_mismatches)
print("\n📄 Written to: final_mismatches.csv")
