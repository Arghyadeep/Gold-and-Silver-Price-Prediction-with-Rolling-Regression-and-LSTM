#dependencies
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd
from dateutil import parser

urls = {'gold':'https://www.investing.com/commodities/gold-historical-data',
        'silver':'https://www.investing.com/commodities/silver-historical-data'}

def fetch_data(url):
    """
    This function takes an url as parameter and fetches the targeted tables in a webpage.
    It returns a bs4 object which is further used to fetch values from the table.
    """
    
    temp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    content_page = soup(temp.content,'html.parser')
    containers = content_page.findAll('table', {'class':'genTbl closedTbl historicalTbl'})
    return containers

def create_dataframe(container):
    """
    This function takes the bs4 object and extracts data from it. The data is saved in
    separate arrays such that the indices of these arrays forms individual rows in the
    final dataframe. The function returns a dataframe which contains extracted data from
    the parsed table.
    """
    
    dates = []
    prices = []
    opens = []
    highs = []
    lows = []
    for table in container:
        i = 0
        for td in table.findAll('td'):
            i += 1
            if i == 1:
                date = parser.parse(td.text)
                dates.append(date)
            if i >= 2 and i <= 5:
                temp = td.text.replace(",","")
            if i == 2:
                prices.append(float(temp))
            if i == 3:
                opens.append(float(temp))
            if i == 4:
                highs.append(float(temp))
            if i == 5:
                lows.append(float(temp))
            if i == 7:
                i = 0
    df = pd.DataFrame({'date':np.array(dates),'open':np.array(opens),
                       'price':np.array(prices),'high':np.array(highs),
                       'low':np.array(lows)})
    return df
    

def save_data(commodity):
    url = urls[commodity]
    container = fetch_data(url)
    df = create_dataframe(container)
    outfile = commodity + ".csv"
    df.to_csv(outfile)

save_data("gold")
save_data("silver")
print("Data saved as CSV file succesfully!")
    


