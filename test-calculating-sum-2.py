import pandas as pd
import numpy as np
import pyttsx
df = pd.read_excel("1.xlsx")


df["values"].sum(), df["values"].mean(),df["values"].min(),df["values"].max()
df.head()
print(df["values"].sum())
print(df["values"].mean())
print(df["values"].min())
print(df["values"].max())

#Trying to print data to cell directly--------------Needs to be modified
#df.iloc[16][1] = df["values"].sum()
df.set_value(11,'Sum',df["values"].sum())
df.to_excel('1.xlsx', index=False)


engine = pyttsx.init()
engine.say(df["values"].sum())
engine.runAndWait()