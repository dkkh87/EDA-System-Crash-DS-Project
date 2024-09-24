import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print ("======================= FIRST 5 ROWS  ================================")
df = pd.read_csv('device_crash_dataset.csv')
print(df.head(5))

print ("======================= LAST 5 ROWS  ================================")
print(df.tail(5))

print ("======================= SHAPE  ================================")
print(df.shape)

print ("======================= INFO  ================================")
print(df.info())

print ("======================= DESCRIBE  ================================")
print(df.describe())

print ("======================= NULL  ================================")
print(df.isnull().sum())

print ("======================= HISTOGRAM  ================================")
sns.histplot(df["CPU Usage (%)"], bins=15)
plt.title("CPU USAGE HISTOGRAM")
plt.show()
sns.histplot(df["Memory Usage (MB)"], bins = 15)
plt.title("MEMORY USAGE HISTOGRAM")
plt.show()
sns.histplot(df["Disk Usage (%)"], bins = 15)
plt.title("DISK USAGE HISTOGRAM")
plt.show()
sns.histplot(df["Network Activity (MB/s)"], bins = 15)
plt.title("NETWORK USAGE HISTOGRAM")
plt.show()
sns.histplot(df["Temperature (°C)"], bins = 15)
plt.title("NETWORK USAGE HISTOGRAM")
plt.show()
sns.histplot(df["GPU Usage (%)"], bins = 15)
plt.title("NETWORK USAGE HISTOGRAM")
plt.show()
