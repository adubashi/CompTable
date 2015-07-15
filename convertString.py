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
