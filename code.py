import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR/"data"/"input"/"athletes.csv"

df = pd.read_csv(INPUT_FILE)

#Exercise 1

print(df.head()) #to see first rows of a data frame
print(df.info()) #to see dtype and null count of a data frame
print(df.describe()) #to see statistical info of int/float columns - mean / median / min / max

#Exercise 2

q1 = df[df['age']>30] #all members older than 30 years old
q2 = df[(df['sex']=='F') & (df['weight']<65)] #women lighter than 65kg
q3 = df[df['city'].isin(['Tehran','Mashhad'])] #All members from Tehran or Mashhad
q4 = df[['first_name', 'age', 'city']].head(5) #First name, age and city of first five people


print(q4)
