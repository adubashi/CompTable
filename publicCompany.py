import stockretriever
import convertString




class publicCompany():
    def getData(self):
        info = stockretriever.get_current_info([self.ticker])
        self.sharePrice = float(info['Bid'])
        self.marketCap = convertString.convertString(info['MarketCapitalization'])
        self.ebitda = convertString.convertString(info['EBITDA'])
        self.eps = info['EPSEstimateCurrentYear']
        #Equity Multiples 
        self.PEGRatio = info['PEGRatio']
        self.PERatio = info['PERatio']
        self.PriceBook = info['PriceBook']
        
        self.calculateEnterpriseValue();
        
        self.amortization = float(raw_input("Enter Amortization:"))
        self.depreciation = float(raw_input("Enter Depreciation:"))
        
        self.sales = float(raw_input("Enter Sales:"))
        self.UnleveredFreeCashFlow = float(raw_input("Enter Unlevered Free Cash Flow:"))
        
        
        self.EBIT = self.ebitda - self.amortization - self.depreciation
        #Enterprise Values
        print self.ebitda
        #print self.enterpriseValue
        self.evEBITDA = self.enterpriseValue/self.ebitda
        self.evEBIT = self.enterpriseValue/self.EBIT
        self.evSales = self.enterpriseValue/self.sales
        self.evUnleveredCF = self.enterpriseValue/self.UnleveredFreeCashFlow


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
        
        #Components of EBITDA
        self.depreciation = 0
        self.amortization = 0
        
        #Equity Multiples
        self.PEGRatio = ""
        self.PERatio = ""
        self.PriceBook = ""
        
        self.EBIT = 0
        self.depreciation = 0
        self.amortization = 0
        
        self.sales = 0
        self.UnleveredFreeCashFlow = 0
        #EnterpriseValue Multiples
        self.evEBITDA = 0
        self.evEBIT = 0
        self.evSales = 0
        self.evUnleveredCF = 0
        self.getData()
        
        

    def toString(self):
        print self.ticker
        print 'Share Price' +  ": " + str(self.sharePrice)
        print 'Ebitda' +  ": " + str(self.ebitda)
        print 'Market Cap' +  ": " + str(self.marketCap)
        print 'EPS estimate current year' +  ": " + str(self.eps)
        
        print 'EQUITY MULTIPLES'
        print 'PEG ratio' + ": " + str(self.PEGRatio)
        print 'PE ratio' + ": " + str(self.PERatio)
        print 'PriceBook' + ": "+ str(self.PriceBook)
        
        print 'ENTERPRISE VALUE MULTIPLES'
        print 'evEBITDA' + ": " + str(self.evEBITDA)
        print 'evEBIT' + ": " + str(self.evEBIT)
        print 'evSales' + ": "+ str(self.evSales)
        print 'evUnleveredCF' + ": "+ str(self.evUnleveredCF)
    
                   
    def calculateEnterpriseValue(self):
        _equityValue = self.marketCap;
        _debt = float(raw_input("Enter Debt:"))
        _preferredStock = float(raw_input("Enter Preferred Stock"))
        _minorityInterests = float(raw_input("Enter Minority Interests:"))
        _cash = float(raw_input("Enter Cash and Cash Equivalents:"))
        self.enterpriseValue = _equityValue + _debt + _preferredStock + _minorityInterests - _cash


Company = publicCompany('AAPL')
Company.toString()

