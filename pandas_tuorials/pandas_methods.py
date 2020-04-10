import pandas as pd 
import numpy as np 

df = pd.read_csv("insurance (2).csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head())

print(df.tail())

print(df.columns)

print(df.isnull().sum())

df.loc[df.region == 'southwest', 'region'] = np.nan
df.loc[df.children == 1, 'children'] = np.nan

print(df.isnull().sum())

print("Length Before:", len(df))
df.dropna(inplace = True)
print("Length After:", len(df))

print(df.isnull().sum())

df = df[df['charges'] > 10000]
print(df.head())


print("Maximum Value: ", df['charges'].max())

print("Minimum Value: ", df['charges'].min())

print("Maximum Value: ", df['age'].max())
print("Minimum Value: ", df['age'].min())

print("Maximum Value: ", df['bmi'].max())
print("Minimum Value: ", df['bmi'].min())

for index, rows in df.iterrows():
    print('sex:', rows['sex'], 'charges:', rows['charges'], 'smoker:', rows['smoker'])

for index, rows in df.iterrows():
    if (rows.sex == 'female') and (rows.smoker == 'yes'): 
        df.at[index, 'female_smoker'] = True
    else:
        df.at[index, 'female_smoker'] = False
        
        
for index, rows in df.iterrows():
    if (rows.sex == 'male') and (rows.smoker == 'yes') and (rows.age > 50) and (rows.children > 0): 
        df.at[index, 'male_smoker_with_children'] = True
    else:
        df.at[index, 'male_smoker_with_children'] = False

print(df.head())

from collections import Counter
print(Counter(df['female_smoker']))

print(Counter(df['male_smoker_with_children']))


df_female = df[df['sex'] == 'female']
df_male = df[df['sex'] == 'male']

print("Female charges: ", df_female['charges'].mean())
print("Male charges: ", df_male['charges'].mean())

#df = df.loc[(df.sex == 'female') & (df.smoker == 'yes') & (df.age >= 50)]
#df.reset_index(inplace=True)
#del df['index']
#print(df.head())



print(df.head())
print("---------------------First---------------------")
print(df.iloc[0])
print("---------------------Second---------------------") 
print(df.iloc[1])
print("---------------------Last---------------------")
print(df.iloc[-1])


print("---------------------First---------------------")
print(df.loc[0, 'sex'])
print("---------------------Second---------------------") 
print(df.loc[1, 'sex'])


print("---------------------First---------------------")
print(df.loc[0:3, 'sex'])
print("---------------------Second---------------------") 
print(df.loc[3:6, 'sex'])

df_yes = df[df['smoker'] == 'yes']
df_yes  = df_yes.groupby(['sex'])['smoker'].count()
print(df_yes.head())


df_no = df[df['smoker'] == 'no']
df_no  = df_no.groupby(['sex'])['smoker'].count()
print(df_no.head())

df  = df.groupby(['sex'])['charges'].mean()
print(df.head())


df  = df.groupby(['region'])['charges'].mean()
print(df.head())


df  = df.groupby(['smoker', 'sex'])['charges'].mean()
print(df.head())


df  = df.groupby(['sex'])['charges'].std()
print(df.head())

df  = df.groupby(['smoker', 'sex'])['charges'].std()
print(df.head())

