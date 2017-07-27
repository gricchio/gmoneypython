'''
Created on Dec 7, 2016

@author: riccga
'''
import pandas as pd
import numpy as np
import xlrd as xlrd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

np.seed(111)

def Createdataset(number=1):
    Output = []
    
    for i in range(number):
        rng = pd.date_range(start = '1/1/2016', end='12/31/2016', freq='W-MON')
        data = np.randint(low=25,high=1000,size=len(rng))
        status = [1,2,3]
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        states = ['GA','FL','fl','NY','NJ','TX']
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
        Output.extend(zip(random_states, random_status, data, rng))
    return Output

dataset = Createdataset(4)

df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
print df.head()



msft = pd.read_excel("data/Excelbook1.xlsx")

age = msft['Age']

#can select a number within age by doing a slice []

for number in age:
    print number

print age.mean().round(4)
print age.sum().round(2)


    


