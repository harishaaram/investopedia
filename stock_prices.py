import urllib
from bs4 import BeautifulSoup
import requests
import re
#from Online_alram import alert

# Description: This program reads user stock symbol and target value of
# stock price from the realtime stock market and alerts the user.
#
# input: textfile containing the stocksymbol-targetprice,(eg: AAPL-140,)
# NOTE: '-' links the symbol with price and ',' terminates
#
#  output: alert if the market price matches the users target price

dir_path = "/home/harish/Desktop/test/"
url = 'http://finance.yahoo.com/quotes/'

filename = "Readme.txt"
fread = open(dir_path+filename,'r').read()

#replace the newline from the file
str2 = fread.replace("\n","-")

#split the symbol and target price
splitedlist = str2.split('-')
print splitedlist

def scrap_marketstockprice(url):
    dta = requests.get(url).text
    soup = BeautifulSoup(dta, 'html.parser')
    price = soup.find_all(class_=["col-price", "invalid-symbol"])
    price = [next(x.strings) for x in price]
    # fix up ': '
    price = [x.replace(': ','') for x in price]
    print(price)

def concatenate_symbols(splitedlist, url):
#concatenate stock symbols into string
    # eg: http://finance.yahoo.com/quotes/AAPL,GOOG
    i =0
    symbol_list = ''
    while i <= len(splitedlist):
        if symbol_list=='':
            symbol_list = splitedlist[i]
        else:
            symbol_list = symbol_list + ',' + splitedlist[i]
        i = i+2
    scrap_marketstockprice(url+symbol_list)

#get the stock price:
concatenate_symbols(splitedlist,url)