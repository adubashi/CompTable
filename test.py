import stockretriever
import json
stocks = stockretriever

def getData(ticker):
    info = stocks.get_current_info([ticker])

    print info['Bid']
    print info['MarketCapitalization']
    print info['EBITDA']


def convertString(number):
    sign = 0;
    #get sign and strip it
    if(number[0] == '-'):
        sign = -1
        number = number[1:]
    else:
        sign = 1
    #get multiple
    numberDict = {};
    numberDict['M'] = 1000000
    numberDict['B'] = 1000000000

    #return total
    multiple = numberDict[number[len(number)-1]]
    number = number[:-1]
    return float(number) * float(sign) * float(multiple)
    
    

#Low market cap



#print json.dumps(info, indent=4, sort_keys=True)

#HIGH market cap



#print json.dumps(info, indent=4, sort_keys=True)

print 'APPLE'
getData("AAPL")
print 'MICROSOFT'
getData("MSFT")
print 'BULLSHIT'
getData("XUE")


print convertString("-10M")





