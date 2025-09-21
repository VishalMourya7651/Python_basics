import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset=pd.read_csv(r"G:\Downlod G\f1.csv")
#print(dataset.head(10))
#print(dataset.shape)
#print(dataset.isnull().sum()/dataset.shape[0]*100 #percentage of missing values
#print(dataset.notnull().sum()/dataset.shape[0]*100)
#sns.heatmap(dataset.isnull())
#plt.show()
#dataset.drop(columns=["LoanAmount"], inplace=True)  
dataset.fillna(method="bfill",inplace=True)  
print(dataset.head(22))

 