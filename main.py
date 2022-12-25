import yfinance as yf



def analyze_cash_flow(stock):
    # analyzes cash flow year over year for a given stock
    # stock parameter must be a yf.ticker data type 
    # returns a dictionary with the percent change in cashflow from last year 

    # Get pandas data frame 
    cashFlow = stock.cashflow 

    # Data frame to list containing the free cash flow each year 
    freeCashFlowLst = cashFlow.iloc[-1].tolist()

    # Gets the keys of free cash flow, which is just the date 
    freeCashFlowKeys = cashFlow.iloc[-1].keys() 

    print(cashFlow.iloc[-1])
    #print(cashFlow.iloc[-1].keys()[0].year)

    i = 0
    perChangeDict = {}
    while (i + 1 != len(freeCashFlowLst)):
        
        # Percent change from last year as a float 
        perChange = float((freeCashFlowLst[i] - freeCashFlowLst[i+1]) / freeCashFlowLst[i+1])*100
        perChange = round(perChange, 2) 

        # appends percent change in a dict per year 
        perChangeDict[freeCashFlowKeys[i].year] = perChange
        i+=1 


    return perChangeDict 




def main(): 
    ticker = input("Input the stock ticker to analyze: ")
    #ticker = "AAPL" 

    stock = yf.Ticker(ticker) 

    cashFlowDict = analyze_cash_flow(stock) 

    print(f"{ticker} cash flow change percent (from prev year): {cashFlowDict}")


    
    #print(cashFlow[0])

    print()


main() 