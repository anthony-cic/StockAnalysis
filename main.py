import yfinance as yf

from perChange import perChange

def main(): 
    ticker = input("Input the stock ticker to analyze: ")
    #ticker = "AAPL" 

    stock = yf.Ticker(ticker) 

    print(f"=================================== \n{ticker} Stock Analysis...\n")

    cashFlow = stock.cashflow 
    cashFlowDict = perChange(cashFlow, 'Free Cash Flow')

    print(f"Free Cash Flow change percent (from prev year): {cashFlowDict}")

    income_stmt = stock.income_stmt
    revenueDict = perChange(income_stmt, 'Total Revenue')

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