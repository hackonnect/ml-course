import pandas as pd
import numpy as np

# Let's retrieve the dataframe we used first
df = pd.read_csv(r'df.csv')

# X = features. y = result.
# In this case, X will be everything BUT the score, while y will be the score.

# Let's print X and see what it's like.
print(df)

# Okay, so we have this column called 'Unnamed: 0'.
# What is it? This appeared because when we saved our panda dataframe, indices were assigned.
# We do not actually need these indices so we can drop this column.

X = df.drop(['Unnamed: 0', 'score'], axis = 1)
y = df['score']

# Let's use sklearn for splitting the datasets.
# We need training and testing data. (Explain in more detail on whiteboard.)

# Here are the funcitons we will use
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
model = LinearRegression()
model.fit(X_train, y_train)

# That's it! Now that our model is trained using Linear Regression
# Let's see how good our training model is (it's score)
# We can use predict() in order to predict the results from a matrix:
y_predict = model.predict(X_test)

# There are many different ways we can see how good our predictions are.
# Exercise: try to find the average difference between the predicted and actual values.
# Hint: you can subtract lists and sum it up using sum(abs(list1 - list2))

print(sum(abs(y_predict - y_test)) / len(y_predict))

# There are also ways we can predict a single result.
# Remember however, model.predict() only takes matrices as input.
# This means that your single test data will have to be a 1xn matrix.
# Simply use double square brackets.

print(model.predict([[0,0,0,1,0,0,4,0,1]]))

# So our model is pretty good, predicting within 30 marks of the actual score consistently.
# So that we do not have to retrain our model everytime we run our program, let's save our model.

import pickle
filename = 'model'
with open(filename, 'wb') as handle:
    pickle.dump(model, handle)

# Now let's load the two models and compare them.
# Remebmer that you always need to import LinearRegression from sklearn.linear_model if you have not earlier in the file.
with open(filename, 'rb') as handle:
    model_from_file = pickle.load(handle)

print(model_from_file.predict([[0,0,0,1,0,0,4,0,1]])) # This should be the same as your previous result.

# We can train our models, save it to a file. When we want to use it in another file or in our project, we can load it.
# Extension task 1: try to build a console application that lets people input their information and predict their total score.
# Extension task 2: ask your course teacher/instructor for more information about logistic regression and classification algorithms.
# We've only touched the tip of the iceberg for machine learning. If you want to learn more about different algorithms and how they are used, please do not hesitate to contact our tech support team.