import yfinance as yf



def analyze(df, key):
    # analyzes a key year over year for a given stock
    # stock parameter must be a yf.ticker data type 
    # returns a dictionary with the percent change in cashflow from last year 


    i = 0 
    perChangeDict = {} 
    for date in df.keys():
        if (i + 1 == len(df.keys())):
            break 

        amt = df[date][key]
        prev = df[df.keys()[i+1]][key]

        perChange = float((amt - prev) / prev)*100
        perChange = round(perChange, 2) 

        perChangeDict[df.keys()[i].year] = perChange
        i += 1
    
    return perChangeDict



def main(): 
    #ticker = input("Input the stock ticker to analyze: ")
    ticker = "AAPL" 

    stock = yf.Ticker(ticker) 

    print(f"=================================== \n{ticker} Stock Analysis...\n")

    cashFlow = stock.cashflow 
    cashFlowDict = analyze(cashFlow, 'Free Cash Flow')

    print(f"Free Cash Flow change percent (from prev year): {cashFlowDict}")

    income_stmt = stock.income_stmt
    revenueDict = analyze(income_stmt, 'Total Revenue')

    print(f"Revenue change percent (from prev year): {revenueDict}")
    
    # current stock price 
    currentPrice = stock.info['currentPrice'] 
    
    # last years date 
    date = income_stmt.keys()[1] 
    # last reported EPS 
    EPS = income_stmt[date]['Diluted EPS'] # all convertible securities exerised
    PE = currentPrice / EPS
    PE = round(PE, 2)
    print(f"PE: {PE}")

    print(f" 52 Week Change {stock.info['SandP52WeekChange']}") 


    print("=================================== \n")


main() 