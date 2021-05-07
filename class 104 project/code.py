import statistics 
import pandas as pd
import csv
df = pd.read_csv(r"/Users/muraliganguri/Downloads/class 104 project/SOCR-HeightWeight.csv")
weight = df["Weight(Pounds)"].tolist()
x = statistics.mean(weight)
y = statistics.mode(weight)
z = statistics.median(weight)
print("The mean of weight",x)
print("The mode of weight",y)
print("The median of weight",z)