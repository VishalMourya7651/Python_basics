import pandas as pd
df=pd.DataFrame({"name":["cow","cat","wscude","dog","black"]})
#print(df)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["en_name"]=le.fit_transform(df["name"])
print(df)