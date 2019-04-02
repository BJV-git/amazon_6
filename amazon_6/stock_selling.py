# Just add when ever the difference is opsitive

def stock_profit(stocks):
    return sum(max(stocks[i+1]-stocks[i], 0) for i in range(len(stocks)-1))