from django.shortcuts import render
from tasks import fetch_data
import redis
from django.conf import settings

# Create your views here.
# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)

def main(request):
    return render(request, 'cards.html')


def create_cards(request,**kwargs):
    if request.method == "POST":
        stocks_list = ['BPCL','IOC','POWERGRID','JSWSTEEL','TITAN','ONGC','INFY','SHREECEM']
        stock_price = []

        for stock in stocks_list:

            # data = fetch_data(stock) # Synchronous call
            data = fetch_data.delay(stock) # Asynchronous call

            stock_price.append(data)
        print(stock_price)

        # Adding data to redis instance
        # redis_instance.set(kwargs['stock_key'], stock_price)

    return render(request, 'cards.html')

# def cards_val(request, **kwargs):
#     stock_val = redis_instance.get(kwargs['stock_key'])
#     return render(request, 'cards.html', {'stock_val':stock_val})
