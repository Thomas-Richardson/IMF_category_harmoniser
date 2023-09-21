import pandas as pd
import numpy as np
import random as rd

# How many rows should our data have?
n_rows = 1000

# Make up some categories
IMF_categories= [
    "Staple foods",
    "cigarrettes",
    "shoes",
    "DVDs",
    "vegan schwarma"
    ]

simulated_data = pd.DataFrame({
		"Household_ID": list(range(1, n_rows+1)),
		'Consumption': np.random.uniform(low=1, high=10, size=n_rows),
        "consumption_category": rd.choices(IMF_categories, k= n_rows), 
		})
 
simulated_data.to_csv("IMF_category_harmoniser/Data/simulated_IMF_app_data.csv", index= False)