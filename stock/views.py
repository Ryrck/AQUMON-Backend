import datetime
import json
from django.db.models import Max, Min
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from stock.models import Stock
import requests

# Create your views here.
def stock_api(request):
    new_obj = Stock()
    new_obj.stock_symbol = "TSLA"
    new_obj.stock_price = 10
    new_obj.stock_date = datetime.datetime.now()
    new_obj.save()
    return JsonResponse(data = {'msg': 'New stock success.'}, status = 200)

def get_stock(request):
    if request.method == "GET":
        data = request.GET.dict()
        query_stock_symbol = data["symbol"]
        query_stock_start = data["start"]
        query_stock_end = data["end"]
        stock_obj = Stock.objects \
                         .filter(stock_symbol__exact = query_stock_symbol) \
                         .filter(stock_date__gte = query_stock_start) \
                         .filter(stock_date__lte = query_stock_end)
        max_price = stock_obj.aggregate(Max('stock_price'))['stock_price__max']
        min_price = stock_obj.aggregate(Min('stock_price'))['stock_price__min']
        mdd = (max_price - min_price) *100/ max_price
        record = []
        for e in stock_obj.all():
            record_list = [e.stock_symbol, e.stock_price, e.stock_date]
            record.append(record_list)
        return JsonResponse(data = {'Maximum Drawdown (in %)': mdd,'Historical record': record}, status = 200)

@csrf_exempt


def add_stock(request):
    if request.method == "POST":
        data = json.loads(request.body)["stock"]
        headers = {
            'Content-Type': 'application/json'
        }
        for i in data:
            requestResponse = requests.get(
                "https://api.tiingo.com/tiingo/daily/{symbol}/prices?startDate={start_date}&endDate={end_date}&token=d35cafc284131bf40deb9ce194b77f6f22884cf5".format(symbol= i["symbol"],start_date =i["start_date"], end_date = i["end_date"]),
                headers=headers)

            for j in requestResponse.json():
                new_obj = Stock()
                new_obj.stock_symbol = i["symbol"]
                new_obj.stock_price = j["close"]
                new_obj.stock_date = j["date"]
                new_obj.save()
        return JsonResponse(data = {'msg': 'Stock updated.'}, status = 200)

@csrf_exempt
def delete_stock(request):
    if request.method == "DELETE":
        data = json.loads(request.body)["stock"]
        for i in data:
            print(i["symbol"])
            stock_obj = Stock.objects.filter(stock_symbol__exact = i["symbol"])
            stock_obj.delete()
        return JsonResponse(data = {'msg': 'delete successfully.'}, status = 200)

def clear_table(request):
    all_obj = Stock.objects.all()
    all_obj.delete()
    return JsonResponse(data = {'msg': 'clear table success.'}, status = 200)

