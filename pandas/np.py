import pandas as pd
arr=pd.DataFrame({
    "name":['vishal','harshit','vinit','Ashish'],
    "   roll_no.":[63,56,61,80],
    "       city":['gorakhpur','ludhiana','bihar','jharkhand']
})
print(arr.to_string(index=False))
f = pd.read_csv("G:\\Downlod G\\f.csv")
print(arr.shape)

