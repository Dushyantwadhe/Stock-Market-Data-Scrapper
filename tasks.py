from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')

from bs4 import BeautifulSoup
import requests

import redis
# conn = redis.Redis('localhost')

from bs4 import BeautifulSoup
import requests

@app.task
def fetch_data(stockcode):
    # stockcode = "SBIN"
    stock_url  = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")

    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item)+1
            print("Index -> "+ str(index))
            latestPrice=data_array[index].split('"')[1]
            print(latestPrice)
    return latestPrice
