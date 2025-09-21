import pandas as pd
import matplotlib.pyplot as plt
data={
    "cricket Bat": ["SG","BDM","SS","MRF"],
    "COST":[1000, 1500, 1200, 1800],
    "Weigght":[100, 120, 110, 130]
}
dataframe=pd.DataFrame(data)
plt.plot(dataframe["cricket Bat"],dataframe["COST"])
plt.show()