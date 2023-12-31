# INF601 - Advanced Programming in Python
# Dustin Riley
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pathlib as Path

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    # get historical market data past 10 days
    hist = stock.history("10d")

    closingList = []
    # get Close prices for past 10 days
    for price in hist['Close']:
        closingList.append(round(price,2))

    return closingList

#create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# microsoft = MSFT
# walmart = WMT
# paypal = PYPL
# apple = AAPL
# Unity Software Inc. = U

stocks = ["MSFT","WMT","PYPL","AAPL","U"]

# (10/10 points) Store this information in a list that you will convert to a array in NumPy.

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    # plot the graph
    plt.plot(stockClosing)
    # get closing prices and sort them for axis
    prices = getClosing(stock)
    prices.sort()

    # set axis highs and lows
    plt.axis([1,10,prices[0]-2,prices[-1]+2])

    # set graph labels
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # show the graph
    plt.show()
    # save the graph to charts folder
    plt.savefig("charts/" + stock + ".png")




# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.