import publicCompany


class multiples:
    def __init__(self, ticker):
        self.originalCompany = publicCompany.publicCompany(ticker)
        self.compList = []
        self.PElist = []
    def add(self,ticker):
        company = publicCompany.publicCompany(ticker)
        self.compList.append(company)

        #PE multiples
        newList = [];
        newList.append(ticker)
        newList.append(float(company.PERatio))
        self.PElist.append(newList)
        self.PElist.sort(key=lambda x: x[1])
    def toString(self):
        self.originalCompany.toString()
        for i in range(len(self.compList)):
            self.compList[i].toString()
    def printPElist(self):
        print self.PElist
    def sortPElist(self):
        self.PElist.sort(key=lambda x: x[1])
        
        
            

test = multiples("AAPL")
test.add("MSFT")
test.add("JNJ")
test.add("WFC")
test.add("JPM")
test.add("PG")
test.printPElist()

        
        
