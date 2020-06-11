import os 
import numpy as np 
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)

coinbaseFile = '/Users/computer/Documents/bitcoinData/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'
bitstampFile = '/Users/computer/Documents/bitcoinData/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv' 

def getBitstampData(filePath = bitstampFile):
	data = pd.read_csv(filePath)
	#Print the number of missing rows 
	print(data.info())
	data['Date'] = pd.to_datetime(data['Timestamp'],unit = 's')
	print(data.isnull().sum())
	data.dropna(axis = 0,inplace = True)
	index = range(0,len(data))
	data['Index'] = index
	data.set_index('Index',inplace = True)
	print("\n")
	print(data.info())
	data.drop(columns = ['Timestamp'],inplace = True)
	data = data[['Date','Open','High','Low','Close','Volume_(BTC)','Volume_(Currency)','Weighted_Price']]
	return data

def coinbaseData(filePath = coinbaseFile):
	data = pd.read_csv(filePath)
	#Print the number of missing rows 
	print(data.info())
	print("\n")
	data['Date'] = pd.to_datetime(data['Timestamp'],unit = 's')
	print(data.isnull().sum())
	data.dropna(axis = 0,inplace = True)
	index = range(0,len(data))
	data['Index'] = index
	data.set_index('Index',inplace = True)
	print(data.info())
	print("\n")
	print(data[:10])
	data.drop(columns = ['Timestamp'],inplace = True)
	data = data[['Date','Open','High','Low','Close','Volume_(BTC)','Volume_(Currency)','Weighted_Price']]
	return data









