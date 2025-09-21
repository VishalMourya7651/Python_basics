import matplotlib.pyplot as plt
import pandas as pd

# Corrected data (assuming Weight=120 instead of 1200)
data = {
    "cricket Bat": ["SG", "BDM", "SS", "MRF"],
    "COST": [1000, 1500, 1200, 1800],
    "Weight": [100, 120, 1200, 130]
}

# Create DataFrame
dataframe = pd.DataFrame(data)

# Plotting COST vs Weight with Bat names as labels
plt.plot(dataframe["cricket Bat"], dataframe["Weight"], marker='o')

plt.grid(True)
plt.show()
