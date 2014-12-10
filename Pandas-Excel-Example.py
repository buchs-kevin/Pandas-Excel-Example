import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# load the sheet into the Pandas Dataframe structure
df = pd.read_excel('Pandas-Example.xlsx', sheetname='Sheet1')

print("The list of row indicies")
print(df.index)
print("The column headings")
print(df.columns)

print("The 'Patient' column information:")
print(df['Patient'])

# print each row of the patient column
for i in df.index:
    print(df['Patient'][i])

# compute a new column as the product of two other columns
for i in df.index:
    df['BP*SO2'][i] = df['BP'][i] * df['SO2'][i]

print("results of column multiplication:")
print(df['BP*SO2'])

# write the dataframe back out with the new column data included
writer = ExcelWriter('Pandas-Example-Out.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

