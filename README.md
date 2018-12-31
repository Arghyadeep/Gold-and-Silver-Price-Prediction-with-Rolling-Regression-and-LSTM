## Gold-and-Silver-Price-Prediction-with-Rolling-Regression-and-LSTM


# Program to fetch the historical prices and dates of gold and silver from URLs.
●	Filename: read_historical_data.py 
●	The file requires no arguments. On running the file the file saves gold and silver historical prices in CSV format in the file location itself.
●	Libraries used: requests, bs4, pandas, dateutil

# Program to calculate the mean and variance of a certain range from stored data.
●	Filename: mean_and_variance.py
●	The file requires 3 arguments to run as mentioned in the task. The program does an extensive check on the correct commodity(gold/silver) as well as the entered dates. Note that the dates should exist in the stored data run from the first program(“read_historical_data.py”). 
●	Libraries used: pandas, numpy, datetime, sys

# The following tasks are performed on a downloaded dataset different from that of the one fetched from program1. Also, it is performed only on Gold prices dataset.
## Program to decide if previous prices are good predictors of future prices.
●	Filename: Predict Future Prices.ipynb
●	This file is a Jupyter Notebook that has multiple cells performing various functions. The program is subdivided into 3 major parts, 
1.	Reading and cleaning data, and creating rolling windows dataset.
2.	Predictions using Linear Regression.
3.	Predictions using an LSTM network.
One needs to run consecutive cells to make things work correctly. Note that each cell is dependent on the previous cell results in the notebook.
●	Libraries used: Pandas, numpy, dateutil, scikit learn, keras, matplotlib

## Program to decide if price increase or decrease is predictable 
●	Filename: increase_or_decrease.py
●	The file does not require any arguments. This prediction is a little different from the previous one. Here, instead of a series of prices, the Open, Close, High and Low values of gold is used to predict the percent changes. The dataset is built accordingly and is trained with a Linear Regression model. The file plots a few predicted data points as well the corresponding true values. It also prints a few random predictions and corresponding true values which gives us a better insight into the accuracy.
●	Libraries used: Pandas, Scikit Learn, Datetime, numpy, sys, random
