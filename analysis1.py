Python 3.7.6 (default, Dec 30 2019, 19:38:28) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable. Visit
http://www.python.org/download/mac/tcltk/ for current information.
>>> 
>>> 
>>> 
>>> file1 = '/Users/computer/Documents/bitcoinData/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv'
>>> coinbaseFile = '/Users/computer/Documents/bitcoinData/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'
>>> import os
>>> import pandas as pd
>>> priceDF = pd.read_csv(file1)
>>> coinbaseDF = pd.read_csv(coinbaseFile)
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4363457 entries, 0 to 4363456
Data columns (total 8 columns):
 #   Column             Dtype  
---  ------             -----  
 0   Timestamp          int64  
 1   Open               float64
 2   High               float64
 3   Low                float64
 4   Close              float64
 5   Volume_(BTC)       float64
 6   Volume_(Currency)  float64
 7   Weighted_Price     float64
dtypes: float64(7), int64(1)
memory usage: 266.3 MB
>>> coinbaseDF.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2099760 entries, 0 to 2099759
Data columns (total 8 columns):
 #   Column             Dtype  
---  ------             -----  
 0   Timestamp          int64  
 1   Open               float64
 2   High               float64
 3   Low                float64
 4   Close              float64
 5   Volume_(BTC)       float64
 6   Volume_(Currency)  float64
 7   Weighted_Price     float64
dtypes: float64(7), int64(1)
memory usage: 128.2 MB
>>> priceDF.dropna(axis = 0,inplace = True)
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3126480 entries, 0 to 4363456
Data columns (total 8 columns):
 #   Column             Dtype  
---  ------             -----  
 0   Timestamp          int64  
 1   Open               float64
 2   High               float64
 3   Low                float64
 4   Close              float64
 5   Volume_(BTC)       float64
 6   Volume_(Currency)  float64
 7   Weighted_Price     float64
dtypes: float64(7), int64(1)
memory usage: 214.7 MB
>>> coinbaseDF.dropna(axis = 0,inplace = True)
>>> coinbaseDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1990691 entries, 0 to 2099759
Data columns (total 8 columns):
 #   Column             Dtype  
---  ------             -----  
 0   Timestamp          int64  
 1   Open               float64
 2   High               float64
 3   Low                float64
 4   Close              float64
 5   Volume_(BTC)       float64
 6   Volume_(Currency)  float64
 7   Weighted_Price     float64
dtypes: float64(7), int64(1)
memory usage: 136.7 MB
>>> priceDF['Date'] = pd.to_datetime(priceDF['Timestamp'])
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3126480 entries, 0 to 4363456
Data columns (total 9 columns):
 #   Column             Dtype         
---  ------             -----         
 0   Timestamp          int64         
 1   Open               float64       
 2   High               float64       
 3   Low                float64       
 4   Close              float64       
 5   Volume_(BTC)       float64       
 6   Volume_(Currency)  float64       
 7   Weighted_Price     float64       
 8   Date               datetime64[ns]
dtypes: datetime64[ns](1), float64(7), int64(1)
memory usage: 238.5 MB
>>> priceDF[:10]
       Timestamp  Open  ...  Weighted_Price                          Date
0     1325317920  4.39  ...        4.390000 1970-01-01 00:00:01.325317920
478   1325346600  4.39  ...        4.390000 1970-01-01 00:00:01.325346600
547   1325350740  4.50  ...        4.526411 1970-01-01 00:00:01.325350740
548   1325350800  4.58  ...        4.580000 1970-01-01 00:00:01.325350800
1224  1325391360  4.58  ...        4.580000 1970-01-01 00:00:01.325391360
1896  1325431680  4.84  ...        4.840000 1970-01-01 00:00:01.325431680
2333  1325457900  5.00  ...        5.000000 1970-01-01 00:00:01.325457900
3612  1325534640  5.00  ...        5.000000 1970-01-01 00:00:01.325534640
4553  1325591100  5.32  ...        5.320000 1970-01-01 00:00:01.325591100
4710  1325600520  5.14  ...        5.140000 1970-01-01 00:00:01.325600520

[10 rows x 9 columns]
>>> priceDF.drop(columns = ['Date'],inplace = True)
>>> priceDF['Date'] = pd.to_datetime(priceDF['Timestamp'],infer_datetime_format = True)
>>> priceDF[:10]
       Timestamp  Open  ...  Weighted_Price                          Date
0     1325317920  4.39  ...        4.390000 1970-01-01 00:00:01.325317920
478   1325346600  4.39  ...        4.390000 1970-01-01 00:00:01.325346600
547   1325350740  4.50  ...        4.526411 1970-01-01 00:00:01.325350740
548   1325350800  4.58  ...        4.580000 1970-01-01 00:00:01.325350800
1224  1325391360  4.58  ...        4.580000 1970-01-01 00:00:01.325391360
1896  1325431680  4.84  ...        4.840000 1970-01-01 00:00:01.325431680
2333  1325457900  5.00  ...        5.000000 1970-01-01 00:00:01.325457900
3612  1325534640  5.00  ...        5.000000 1970-01-01 00:00:01.325534640
4553  1325591100  5.32  ...        5.320000 1970-01-01 00:00:01.325591100
4710  1325600520  5.14  ...        5.140000 1970-01-01 00:00:01.325600520

[10 rows x 9 columns]
>>> priceDF.drop(columns = ['Date'],inplace = True)
>>> priceDF['Date'] = pd.to_datetime(priceDF['Timestamp'],unit = 's')
>>> priceDF[:10]
       Timestamp  Open  ...  Weighted_Price                Date
0     1325317920  4.39  ...        4.390000 2011-12-31 07:52:00
478   1325346600  4.39  ...        4.390000 2011-12-31 15:50:00
547   1325350740  4.50  ...        4.526411 2011-12-31 16:59:00
548   1325350800  4.58  ...        4.580000 2011-12-31 17:00:00
1224  1325391360  4.58  ...        4.580000 2012-01-01 04:16:00
1896  1325431680  4.84  ...        4.840000 2012-01-01 15:28:00
2333  1325457900  5.00  ...        5.000000 2012-01-01 22:45:00
3612  1325534640  5.00  ...        5.000000 2012-01-02 20:04:00
4553  1325591100  5.32  ...        5.320000 2012-01-03 11:45:00
4710  1325600520  5.14  ...        5.140000 2012-01-03 14:22:00

[10 rows x 9 columns]
>>> index = range(0,len(priceDF))
>>> max(index)
3126479
>>> priceDF.set_index(index,inplace = True)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    priceDF.set_index(index,inplace = True)
  File "/usr/local/lib/python3.7/site-packages/pandas/core/frame.py", line 4303, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: 'None of [range(0, 3126480)] are in the columns'
>>> priceDF['Index'] = index
>>> priceDF.set_index('Index',inplace = True)
>>> priceDF[:10]
        Timestamp  Open  ...  Weighted_Price                Date
Index                    ...                                    
0      1325317920  4.39  ...        4.390000 2011-12-31 07:52:00
1      1325346600  4.39  ...        4.390000 2011-12-31 15:50:00
2      1325350740  4.50  ...        4.526411 2011-12-31 16:59:00
3      1325350800  4.58  ...        4.580000 2011-12-31 17:00:00
4      1325391360  4.58  ...        4.580000 2012-01-01 04:16:00
5      1325431680  4.84  ...        4.840000 2012-01-01 15:28:00
6      1325457900  5.00  ...        5.000000 2012-01-01 22:45:00
7      1325534640  5.00  ...        5.000000 2012-01-02 20:04:00
8      1325591100  5.32  ...        5.320000 2012-01-03 11:45:00
9      1325600520  5.14  ...        5.140000 2012-01-03 14:22:00

[10 rows x 9 columns]
>>> priceDF.rename(columns = {'Index':''},inplace = True)
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3126480 entries, 0 to 3126479
Data columns (total 9 columns):
 #   Column             Dtype         
---  ------             -----         
 0   Timestamp          int64         
 1   Open               float64       
 2   High               float64       
 3   Low                float64       
 4   Close              float64       
 5   Volume_(BTC)       float64       
 6   Volume_(Currency)  float64       
 7   Weighted_Price     float64       
 8   Date               datetime64[ns]
dtypes: datetime64[ns](1), float64(7), int64(1)
memory usage: 238.5 MB
>>> priceDF.drop(columns = ['Timestamp'],inplace = True)
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3126480 entries, 0 to 3126479
Data columns (total 8 columns):
 #   Column             Dtype         
---  ------             -----         
 0   Open               float64       
 1   High               float64       
 2   Low                float64       
 3   Close              float64       
 4   Volume_(BTC)       float64       
 5   Volume_(Currency)  float64       
 6   Weighted_Price     float64       
 7   Date               datetime64[ns]
dtypes: datetime64[ns](1), float64(7)
memory usage: 214.7 MB
>>> priceDF.isnull().sum()
Open                 0
High                 0
Low                  0
Close                0
Volume_(BTC)         0
Volume_(Currency)    0
Weighted_Price       0
Date                 0
dtype: int64
>>> priceDF = priceDF[['Date','Open','High','Low','Close','Volume_(BTC)','Volume_(Currency)','Weighted_Price']]
>>> priceDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3126480 entries, 0 to 3126479
Data columns (total 8 columns):
 #   Column             Dtype         
---  ------             -----         
 0   Date               datetime64[ns]
 1   Open               float64       
 2   High               float64       
 3   Low                float64       
 4   Close              float64       
 5   Volume_(BTC)       float64       
 6   Volume_(Currency)  float64       
 7   Weighted_Price     float64       
dtypes: datetime64[ns](1), float64(7)
memory usage: 214.7 MB
>>> priceDF[:10]
                     Date  Open  ...  Volume_(Currency)  Weighted_Price
Index                            ...                                   
0     2011-12-31 07:52:00  4.39  ...           2.000000        4.390000
1     2011-12-31 15:50:00  4.39  ...         210.720000        4.390000
2     2011-12-31 16:59:00  4.50  ...         171.380338        4.526411
3     2011-12-31 17:00:00  4.58  ...          41.220000        4.580000
4     2012-01-01 04:16:00  4.58  ...           6.879160        4.580000
5     2012-01-01 15:28:00  4.84  ...          48.400000        4.840000
6     2012-01-01 22:45:00  5.00  ...          50.500000        5.000000
7     2012-01-02 20:04:00  5.00  ...          95.240000        5.000000
8     2012-01-03 11:45:00  5.32  ...          12.870000        5.320000
9     2012-01-03 14:22:00  5.14  ...           3.495200        5.140000

[10 rows x 8 columns]
>>> coinbaseDF['Date'] = pd.to_datetime(coinbaseDF['Timestamp'])
>>> priceDF['Date'] = pd.to_datetime(priceDF['Timestamp'],unit = 's')
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Timestamp'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    priceDF['Date'] = pd.to_datetime(priceDF['Timestamp'],unit = 's')
  File "/usr/local/lib/python3.7/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/usr/local/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Timestamp'
>>> coinbaseDF['Date'] = pd.to_datetime(coinbaseDF['Timestamp'],unit = 's')
>>> coinbaseDF[:10]
       Timestamp    Open  ...  Weighted_Price                Date
0     1417411980  300.00  ...      300.000000 2014-12-01 05:33:00
7     1417412400  300.00  ...      300.000000 2014-12-01 05:40:00
51    1417415040  370.00  ...      370.000000 2014-12-01 06:24:00
77    1417416600  370.00  ...      370.000000 2014-12-01 06:50:00
1436  1417498140  377.00  ...      377.000000 2014-12-02 05:29:00
1766  1417517940  377.75  ...      377.984375 2014-12-02 10:59:00
1771  1417518240  378.00  ...      378.000000 2014-12-02 11:04:00
1772  1417518300  378.00  ...      378.000000 2014-12-02 11:05:00
2230  1417545780  378.00  ...      378.000000 2014-12-02 18:43:00
2245  1417546680  378.00  ...      378.000000 2014-12-02 18:58:00

[10 rows x 9 columns]
>>> coinbaseDF['Index'] = range(0,len(coinbaseDF))
>>> coinbaseDF.set_index('Index',inplace = True)
>>> coinbaseDF[:10]
        Timestamp    Open  ...  Weighted_Price                Date
Index                      ...                                    
0      1417411980  300.00  ...      300.000000 2014-12-01 05:33:00
1      1417412400  300.00  ...      300.000000 2014-12-01 05:40:00
2      1417415040  370.00  ...      370.000000 2014-12-01 06:24:00
3      1417416600  370.00  ...      370.000000 2014-12-01 06:50:00
4      1417498140  377.00  ...      377.000000 2014-12-02 05:29:00
5      1417517940  377.75  ...      377.984375 2014-12-02 10:59:00
6      1417518240  378.00  ...      378.000000 2014-12-02 11:04:00
7      1417518300  378.00  ...      378.000000 2014-12-02 11:05:00
8      1417545780  378.00  ...      378.000000 2014-12-02 18:43:00
9      1417546680  378.00  ...      378.000000 2014-12-02 18:58:00

[10 rows x 9 columns]
>>> coinbaseDF.drop(columns = ['Timestamp'],inplace = True)
\
>>> priceDF = priceDF[['Date','Open','High','Low','Close','Volume_(BTC)','Volume_(Currency)','Weighted_Price']]
>>> coinbaseDF = coinbaseDF[['Date','Open','High','Low','Close','Volume_(BTC)','Volume_(Currency)','Weighted_Price']]
>>> coinbaseDF.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1990691 entries, 0 to 1990690
Data columns (total 8 columns):
 #   Column             Dtype         
---  ------             -----         
 0   Date               datetime64[ns]
 1   Open               float64       
 2   High               float64       
 3   Low                float64       
 4   Close              float64       
 5   Volume_(BTC)       float64       
 6   Volume_(Currency)  float64       
 7   Weighted_Price     float64       
dtypes: datetime64[ns](1), float64(7)
memory usage: 136.7 MB
>>> coinbaseDF[:10]
                     Date    Open  ...  Volume_(Currency)  Weighted_Price
Index                              ...                                   
0     2014-12-01 05:33:00  300.00  ...            3.00000      300.000000
1     2014-12-01 05:40:00  300.00  ...            3.00000      300.000000
2     2014-12-01 06:24:00  370.00  ...            3.70000      370.000000
3     2014-12-01 06:50:00  370.00  ...            9.82555      370.000000
4     2014-12-02 05:29:00  377.00  ...            3.77000      377.000000
5     2014-12-02 10:59:00  377.75  ...         1511.93750      377.984375
6     2014-12-02 11:04:00  378.00  ...         1852.20000      378.000000
7     2014-12-02 11:05:00  378.00  ...         1965.60000      378.000000
8     2014-12-02 18:43:00  378.00  ...           37.80000      378.000000
9     2014-12-02 18:58:00  378.00  ...          299.98080      378.000000

[10 rows x 8 columns]
>>> coinbaseDF.rename(columns = {'Index':''},inplace = True)
>>> coinbaseDF[:10]
                     Date    Open  ...  Volume_(Currency)  Weighted_Price
Index                              ...                                   
0     2014-12-01 05:33:00  300.00  ...            3.00000      300.000000
1     2014-12-01 05:40:00  300.00  ...            3.00000      300.000000
2     2014-12-01 06:24:00  370.00  ...            3.70000      370.000000
3     2014-12-01 06:50:00  370.00  ...            9.82555      370.000000
4     2014-12-02 05:29:00  377.00  ...            3.77000      377.000000
5     2014-12-02 10:59:00  377.75  ...         1511.93750      377.984375
6     2014-12-02 11:04:00  378.00  ...         1852.20000      378.000000
7     2014-12-02 11:05:00  378.00  ...         1965.60000      378.000000
8     2014-12-02 18:43:00  378.00  ...           37.80000      378.000000
9     2014-12-02 18:58:00  378.00  ...          299.98080      378.000000

[10 rows x 8 columns]
>>> 