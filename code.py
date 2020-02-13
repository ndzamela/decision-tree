# --------------
# Importing Necessary libraries
import warnings
warnings.filterwarnings("ignore")
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (10, 8)
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the train data stored in path variable


# Load the test data stored in path1 variable


# necessary to remove rows with incorrect labels in test dataset


# encode target variable as integer



# Plot the distribution of each feature


# convert the data type of Age column in the test data to int type


# cast all float features to int type to keep types consistent between our train and test data

 
# choose categorical and continuous features from data and print them


# fill missing data for catgorical columns


# fill missing data for numerical columns   


# Dummy code Categoricol features


# Check for Column which is not present in test data


# New Zero valued feature in test data for Holand


# Split train and test data into X_train ,y_train,X_test and y_test data


# train a decision tree model then predict our test data and compute the accuracy


# Decision tree with parameter tuning


# Print out optimal maximum depth(i.e. best_params_ attribute of GridSearchCV) and best_score_


#train a decision tree model with best parameter then predict our test data and compute the accuracy




