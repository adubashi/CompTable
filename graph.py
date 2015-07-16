import pylab as plt
import numpy as np
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



def makeBoxPlot(company):
    boxes = []
    totalFigs = 3
    
    graphablePElist = []
    for i in company.PElist:
        graphablePElist.append(i[1])
        
    graphablePEGlist = []
    for i in company.PEGlist:
        graphablePEGlist.append(i[1])
        
    graphablePriceBookList = []
    for i in company.PriceBookList:
        graphablePriceBookList.append(i[1])
        
    boxes.append(graphablePElist)
    boxes.append(graphablePEGlist)
    boxes.append(graphablePriceBookList)
        
        
        
    plt.figure()
    plt.hold = True
    print graphablePElist
    plt.boxplot(boxes, vert = 0)
    plt.title('Equity Value Multiples') 
    plt.text(13, 3.2, "Price to Book ", bbox=dict(facecolor='red', alpha=0.5))
    plt.text(13, 2.2, "PEG ratio ", bbox=dict(facecolor='red', alpha=0.5))
    plt.text(13, 1.3, "PE ratio ", bbox=dict(facecolor='red', alpha=0.5))
    plt.show()

    
    '''
    for i in np.arange(totfigs):    
        x = np.random.random(50)
        #plt.subplot('{0}{1}{2}'.format(totfigs,1,i+1))
        plt.boxplot(x,vert=0)
    '''
    '''
    plt.boxplot(x,vert=0)
    plt.show()
    '''
makeBoxPlot(test)
    
