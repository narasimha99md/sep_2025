import pandas as pd

# Your source data
source_data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, None],  # Null in Age for David
    'Salary': [None, 60000, 70000, 8000],
    'Department': ['HR', 'IT', 'IT', 'HR']
}

# Create DataFrame
df = pd.DataFrame(source_data)

# Find rows where 'Age' is null
null_age_rows = df[df['Age'].isnull()]

# Display the result
print(null_age_rows)

print(type(null_age_rows))
print(df.isnull().sum())



#null_counts[null_counts > 0]

print(df[df.isnull().any(axis=1)])
