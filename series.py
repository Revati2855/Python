import pandas as pd

df = pd.read_csv("student.csv")

s = pd.Series(df["Marks"])

print(s)