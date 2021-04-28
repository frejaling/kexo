from pandas import read_csv
from datetime import datetime

# load data
def parse(x):
    return datetime.strptime(x, '%Y %m %d')
dataset = read_csv('out.csv', index_col=0, delimiter=',', usecols = [i for i in range(3)])
x = dataset.isnull().sum()
print(x)
dataset.fillna(method='ffill', inplace=True)
x = dataset.isnull().sum()
print(x)
# print('här är antalet null: ' + dataset.isnull().sum())
#dataset['SPGTCLEN'] = [float(str(i).replace(',','')) for i in dataset['SPGTCLEN']]
#dataset.drop('No', axis = 1, inplace=True)

# manually specify column names
dataset.columns = ['open', 'oil']
dataset.index.name = 'date'

# mark all NA values with 0 (vi har inga tror jag?)
dataset.fillna(0, inplace=True)


# summarize first 2 rows
print(dataset.head(5))

# save to file
dataset.to_csv('past_returns.csv')