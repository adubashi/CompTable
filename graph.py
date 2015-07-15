from pylab import *
import multiples

test = multiples.multiples("AAPL")
test.add("MSFT")
test.add("JNJ")
test.add("WFC")
test.add("JPM")
test.add("PG")
test.printPElist()

multipleList = test.PElist;
print multipleList
# fake up some data
'''
spread= rand(50) * 100
print spread
center = ones(25) * 50
print center
flier_high = rand(10) * 100 + 100
print flier_high
flier_low = rand(10) * -100
print flier_low
data =(spread, center, flier_high, flier_low)
'''


spread= multipleList[3][1] - multipleList[1][1]
center = multipleList[2][1]
flier_high = multipleList[4][1]
flier_low = multipleList[0][1]
data = (spread, center, flier_high, flier_low)

# basic plot
pylab.boxplot(data,0,'rs',0)
