import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn import linear_model



os.chdir(r'C:\Users\200460\Desktop\Python Projects\ML Project')

pga_data = pd.read_csv("PGATOUR_data2.csv")
pga_data = pga_data[['Player','NUMBER_OF_WINS', 'ROUNDS_PLAYED','AVG_Driving_DISTANCE']]
pga_data = pga_data.rename(columns={'NUMBER_OF_WINS' : 'Wins'})

print 


X = pga_data[['ROUNDS_PLAYED','AVG_Driving_DISTANCE']]
Y = pga_data['Wins']

"""
regr = linear_model.LinearRegression()
regr.fit(X,Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_) 
"""