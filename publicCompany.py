import stockretriever
import convertString




class publicCompany():
    def getData(self):
        info = stockretriever.get_current_info([self.ticker])
        self.sharePrice = float(info['Bid'])
        self.marketCap = info['MarketCapitalization']
        self.ebitda = info['EBITDA']
        self.eps = info['EPSEstimateCurrentYear']
        #Equity Multiples 
        self.PEGRatio = info['PEGRatio']
        self.PERatio = info['PERatio']
        self.PriceBook = info['PriceBook']
        #Enterprise Values
        self.evEBITDA = ""
        self.evEBIT = "";
        self.evSales = ""
        self.evUnleveredCF = "";


    def getData2(self):
        self.sharePrice = 20
        self.ebitda = 1000000
        self.marketCap = 100000
        self.enterpriseValue = 1050000;
        self.eps = 6
        #equity multiples
        self.PEGRatio = "10"
        self.PERatio = "10"
        self.PriceBook = "10"
        #Enterprise Multiples
        self.evEBITDA = ""
        self.evEBIT = "";
        self.evSales = ""
        self.evUnleveredCF = "";
        
    def __init__(self, ticker):
        self.ticker = ticker
        self.sharePrice = 0
        self.ebitda = 0
        self.marketCap = 0
        self.enterpriseValue = 0
        self.eps = 0
        #Equity Multiples
        self.PEGRatio = ""
        self.PERatio = ""
        self.PriceBook = ""
        #EnterpriseValue Multiples
        self.evEBITDA = ""
        self.evEBIT = "";
        self.evSales = ""
        self.evUnleveredCF = "";
        self.getData2()
        
        

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

