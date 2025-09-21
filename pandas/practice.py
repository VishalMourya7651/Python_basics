import pandas as pd
 
dp = pd.DataFrame({
 "name": ['vishal','vinit','harshit','ashish','ravinder'],
    "age": [21, 18, None, 23, None],
    "salary": [900000, 80000, 70000, None, None]
})
  
 print(dp)   # Original DataFrame

 print(dp.isnull().sum())  # Count missing values column-wise

# Replace NaN in salary with mean of salary
dp['salary'].fillna(dp['salary'].mean(), inplace=True)

 print(dp)   # DataFrame after filling salary NaN
