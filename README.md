# wsj-analyst-spreads

###### Description
This program uses the Wall Street Journal API to collect analyst price targets for your target stocks.

As a default, the program takes as input a list of all stocks on the NASDAQ in the stock-names.txt file, and returns two pickle serialized python dictionaries, "ratings_dict_all.pkl" and "extremes.pkl".

The extremes.pkl file contains all tickers with average analyst price target of >Y times current price. (Average price target >= Y * Current Price) The default value for Y is 3. The extremes.pkl file also contains these average target price and current price numbers themselves.

The ratings_dict_all.pkl file returns all tickers along with each of their average, high, low, median target prices and their current price, where these are recorded in the WSJ API. Where these are not recorded, the dictionary entry reads "No analyst ratings recorded."

###### Notes

To run the program, type **"python wsj-analyst-spreads.py"** into your terminal.

This program takes a while to run. If you only need data for a subset of the stocks in the default stock-names.txt file, adjust as needed.

###### Requirements
- Selenium (pip install selenium)


