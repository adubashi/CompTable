import publicCompany


class multiples:
    def __init__(self, ticker):
        self.originalCompany = publicCompany.publicCompany(ticker)
        self.compList = []
        self.PElist = []
        self.PEGlist = []
        self.PriceBookList = []
    def add(self,ticker):
        
        company = publicCompany.publicCompany(ticker)
        self.compList.append(company)

        #PE multiples
        newList = [];
        newList.append(ticker)
        newList.append(float(company.PERatio))
        self.PElist.append(newList)
        self.PElist.sort(key=lambda x: x[1])
        
        #PEG multiples
        PEG = [];
        PEG.append(ticker)
        PEG.append(float(company.PEGRatio))
        self.PEGlist.append(PEG)
        self.PEGlist.sort(key=lambda x: x[1])
        
        #PriceBookValue
        PriceBook = []
        PriceBook.append(ticker)
        PriceBook.append(float(company.PriceBook))
        self.PriceBookList.append(PriceBook)
        self.PriceBookList.sort(key=lambda x: x[1])
        
    def toString(self):
        self.originalCompany.toString()
        for i in range(len(self.compList)):
            self.compList[i].toString()
            
    def printPElist(self):
        print self.PElist
    def printPEGlist(self):
        print self.PEGlist
    def printPriceBook(self):
        print self.PriceBookList
        
    def printEquityMultiples(self):
        print "Equity Multiples"
        print "PE List"
        self.printPElist()
        print "PEG List"
        self.printPEGlist()
        print "PriceBook List"
        self.printPriceBook()
        
        
        
            

test = multiples("AAPL")
test.add("MSFT")
test.add("JNJ")
test.add("WFC")
test.add("JPM")
test.add("PG")
test.printEquityMultiples()

        
        
