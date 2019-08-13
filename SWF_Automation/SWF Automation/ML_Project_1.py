'''
Created on Mar 28, 2018

@author: riccga
'''
import sklearn, scipy, numpy, matplotlib
import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import expon
from scipy.stats import randint



dir = r'C:\Users\200460\Desktop\Python Projects\ML Project'
os.chdir(dir)

data_source = 'PGATOUR_data2.csv'

df = pd.read_csv(data_source)
df = pd.get_dummies(df)

X = pd.DataFrame()
Y = pd.DataFrame()

#add data to X frame

X[['x']] = df['x']
X[['y']] = df['y']

#add data to Y frame
for col in df.columns.values:
    if col not in ['x', 'y']:
        Y[col] = df[col]

#Create separate data sets for training and testing

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3)

# Create pipelines for training machine learning models
# The pipeline for the classification aspect of the problem
pipe_clf = Pipeline([('scl', StandardScaler()), 
                     ('poly', PolynomialFeatures()), 
                     ('clf', LogisticRegression())])
# The pipeline for the regression aspect of the problem
pipe_regr = Pipeline([('scl', StandardScaler()), 
                      ('poly', PolynomialFeatures()), 
                      ('linear', LinearRegression(fit_intercept=False))])

# Create the randomized searches
c_range_clf = expon(scale=1)
tol_range = expon(scale=1e-4)
degree_range = randint(1, 10)

# Define the parameter distribution for the classifier
param_dist_clf = {'poly__degree': degree_range, 
                  'clf__C': c_range_clf, 
                  'clf__tol': tol_range, 
                  'clf__solver': ['newton-cg', 'lbfgs', 'liblinear']}

# Define the parameter distribution for the regressor
param_dist_regr = {'poly__degree': degree_range}

# Initialize the randomized search classifier
rs_clf = RandomizedSearchCV(pipe_clf, 
                            param_dist_clf, 
                            n_iter=300, 
                            scoring='accuracy', 
                            cv=10, 
                            n_jobs=-1, 
                            verbose=1)

# Initialize the randomized search regressor
rs_regr = RandomizedSearchCV(pipe_regr, 
                            param_dist_regr, 
                            n_iter=50, 
                            scoring='r2', 
                            cv=10, 
                            n_jobs=-1, 
                            verbose=1)

# Split the test and training labels for classification and regression
y_train_clf = pd.DataFrame()
y_test_clf = pd.DataFrame()

y_train_regr = pd.DataFrame()
y_test_regr = pd.DataFrame()

for col in y_train.columns.values:
    if 'z' in col:
        # Create regression labels
        y_train_regr[col] = y_train[col]
        y_test_regr[col] = y_test[col]
    else:
        # Create classification labels
        y_train_clf[col] = y_train[col]
        y_test_clf[col] = y_test[col]

if __name__ == '__main__':
    # Put all of your code indented under here
                
    from sklearn.multioutput import MultiOutputClassifier
    
    mo_clf = MultiOutputClassifier(rs_clf)
    
    mo_clf.fit(x_train, y_train_clf)
    rs_regr.fit(x_train, y_train_regr)
    
    print('Test classification score: %.3f' % mo_clf.score(x_test, y_test_clf))
    print('Test regression R2 score: %.3f' % rs_regr.score(x_test, y_test_regr))
    
    import numpy as np
    
    # Plot the decision surfaces of the classifier and regressor
    x = pd.DataFrame(np.linspace(0, 5, 25))
    y = pd.DataFrame(np.linspace(0, 5, 25))
    
    # Create a grid to plot our predicted values over
    surf_x = pd.DataFrame(np.array(np.meshgrid(x, y, )).T.reshape(-1, 2))
    surf_z = pd.DataFrame()    
    
    # Predict a value for each (x, y) pair in the grid
    surf_z['z'] = [x[0] for x in rs_regr.predict(surf_x).tolist()]
        
    # Translate our one-hot encoded labels back into a single list of string values
    category_list = []
    for x in mo_clf.predict(surf_x).tolist():
        if x[0] == 0 and x[1] == 1:
            category_list += ['pos']
        elif x[0] == 1 and x[1] == 0:
            category_list += ['neg']
        else:
            category_list += ['unk']
    
    surf_z['cat'] = category_list
        
    # Separate our values into separate surfaces so we can easily color the different categories from the classifier
    pos_surf = surf_z.copy()
    neg_surf = surf_z.copy()
    unk_surf = surf_z.copy()
        
    # Fill in values that don't match the label with NaN
    pos_surf[pos_surf['cat'] != 'pos'] = np.nan
    neg_surf[neg_surf['cat'] != 'neg'] = np.nan
    unk_surf[unk_surf['cat'] != 'unk'] = np.nan
    
    # Make the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(surf_x[0], surf_x[1], pos_surf['z'], color='b')
    ax.scatter(surf_x[0], surf_x[1], neg_surf['z'], color='r')
    ax.scatter(surf_x[0], surf_x[1], unk_surf['z'], color='g')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
