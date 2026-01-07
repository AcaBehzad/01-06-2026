import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR/"data"/"input"/"athletes.csv"

df = pd.read_csv(INPUT_FILE)

print(df.head()) #to see first rows of a data frame
print(df.info()) #to see dtype and null count of a data frame
print(df.describe()) #to see statistical info of int/float columns - mean / median / min / max


