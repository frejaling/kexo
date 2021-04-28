from pandas import read_csv
from matplotlib import pyplot

# load dataset
dataset = read_csv('past_returns.csv', header=0, index_col=0)
values = dataset.values

# specify colmuns to plot
groups = [0, 1]
i = 1

# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()