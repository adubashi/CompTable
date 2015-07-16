import stockretriever
import convertString




class publicCompany():
    def getData(self):
        info = stockretriever.get_current_info([self.ticker])
        self.sharePrice = float(info['Bid'])
        self.marketCap = info['MarketCapitalization']
        self.ebitda = info['EBITDA']
        self.eps = info['EPSEstimateCurrentYear']
        self.PEGRatio = info['PEGRatio']
        self.PERatio = info['PERatio']
        self.PriceBook = info['PriceBook']
        
    def __init__(self, ticker):
        self.ticker = ticker
        self.ebitda = 0;
        self.marketCap = 0;
        self.enterpriseValue = 0;
        self.eps = 0;
        self.PEGRatio = ""
        self.PERatio = ""
        self.PriceBook = ""
        self.getData()
        
        

    def toString(self):
        print self.ticker
        print 'Share Price' +  ": " + str(self.sharePrice)
        print 'Ebitda' +  ": " + str(self.ebitda)
        print 'Market Cap' +  ": " + str(self.marketCap)
        print 'EPS estimate current year' +  ": " + str(self.eps)
        print 'PEG ratio' + ": " + str(self.PEGRatio)
        print 'PE ratio' + ": " + str(self.PERatio)
        print 'PriceBook' + ": "+ str(self.PriceBook)

               
    def enterpriseValue(self,equityValue,debt,preferredStock,minorityInterests,cash):
        self.enterpriseValue = equityValue + debt + preferredStock + minorityInterests - cash


Company = publicCompany('AAPL')
Company.toString()

