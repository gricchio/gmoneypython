import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson,skellam

os.chdir(r'C:\Users\200460\Desktop\Python Projects\ML Project')

df = pd.read_csv("PGATOUR_data2.csv")
print df.dtypes



