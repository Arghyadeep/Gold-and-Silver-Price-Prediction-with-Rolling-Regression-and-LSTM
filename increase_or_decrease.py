import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
import numpy as np
import sys
import pickle as pkl
from dateutil import parser
from sklearn import linear_model
import random

def read_file(filename):
    try:
        data=pd.read_csv(filename)
        return data
    except:
        print("file not exists or check encoding")

def create_train_data(data):
	"""
	This functions cleans the data by removing unwanted characters and stores them as float values
	in the dataframe. Further it extracts the features and targets and returns them in numpy arrays.
	"""
	data.columns = ['Date','Close','Open','High','Low','Volume','Change%']
	data['Date'] = [parser.parse(dt) for dt in data['Date']]
	data['Close'] = [float(price.replace(",","")) for price in data['Close']]
	data['Open'] = [float(price.replace(",","")) for price in data['Open']]
	data['High'] = [float(price.replace(",","")) for price in data['High']]
	data['Low'] = [float(price.replace(",","")) for price in data['Low']]
	data['Change%'] = [float(percent.replace("%","")) for percent in data['Change%']]
	del data['Volume'] #removing volume since there are many unavailable data which might influence the predictions
	X ,y = [],[]
	for i in range(1,len(data)):
		X.append(list(data.ix[i])[1:5])
		y.append(list(data.ix[i])[5])
	X = np.array(X)[::-1]
	y = np.array(y)[::-1]
	return X,y

def train_test_split(X,y,split):
    split_size = int(split*(len(X)))
    trainX, trainy = X[:split_size], y[:split_size]
    testX,testy = X[split_size:],y[split_size:]
    return trainX, trainy, testX, testy

def train_model(trainX, trainy, testX, testy):
	"""
	Function to train model and return prediction values on test set also Rsquared score on entire
	test set. Note no hyperparamter tuning or model selection has been performed since the idea is
	to verify if we can predict increase or decrease in price.
	"""
	model= linear_model.LinearRegression()
	fit = model.fit(trainX,trainy)
	predictions = fit.predict(testX)
	score = fit.score(testX,testy)
	return score,predictions

def plot_predictions(predictions,true_vals,display_size):
    plt.plot(predictions[-display_size:],color = "red", label = 'predictions')
    plt.plot(true_vals[-display_size:],color = "green", label = 'True values')
    plt.legend(loc = 'upper right')
    plt.title('Prediction vs True values of percent changes in Gold Prices')
    plt.xlabel('Percent changes')
    plt.ylabel('Observations')
    plt.show()
        

filename = "Gold Futures Historical Data.csv"
data = read_file(filename)
X,y = create_train_data(data)
split = 0.9
trainX, trainy, testX, testy = train_test_split(X,y,split)
score,predictions = train_model(trainX, trainy, testX, testy)
print("Rsquared score on test data is", score)
plot_predictions(predictions,testy,50)
print()
print("Random predictions and corresponding True values for comparision")
print()
indices = random.sample(range(len(predictions)),20)
for ind in indices:
        print("Prediction = ","%0.2f"%predictions[ind], "   True Value = ",testy[ind])




