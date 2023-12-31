# INF601 - Advanced Programming in Python
# Lisa Thoms
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.

# (5/5 points) Proper import of packages used.

# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.

# (10/10 points) Store this information in a list that you will convert to a array in NumPy.

# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.

# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.

# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!

# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.

# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.



#function to get closing stock price from all stocks
def getClosing(ticker):
    #get the closing price for the last 10 trading days
    stock = yf.Ticker(ticker)
    # get historical market data
    hist = stock.history(period="10d")

    # create empty closing list
    closingList = []

    # loop through closing prices and add to list
    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList


def printGraph(stock):

    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing) + 1))

    # This plots the graph
    plt.plot(days, stockClosing)

    # get the min and max for y
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set X axis min and max
    # form [xmin, xmax, ymin, ymax]
    plt.axis([10, 1, low_price - 2, high_price + 2])

    # Set label for the graph
    plt.xlabel("Days Ago")
    plt.ylabel("Closing  Price")
    plt.title("Closing Price for " + stock)

    # Saves plot
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # Show graph
    plt.show()


def getStocks():

    global stocks

    print("Please enter 5 stocks to graph: ")
    for i in range(1, 6):

        while True:
            print("Enter stock ticker number: " + str(i))
            ticker = input("> ")
            try:
                print("Checking Ticker")
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                print("Valid Ticker")
                break
            except:
                print("That is not a valid stock. Please enter another.")

    return stocks

stocks = []

# Start of program
try:
    # Create our charts folder
    Path("Charts").mkdir()
except FileExistsError:
    pass

for stock in getStocks():
        getClosing(stock)
        printGraph(stock)

# end project
