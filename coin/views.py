from django.shortcuts import render
import requests
import json
# Create your views here.


def home(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    return render(request,"index.html",{"api":api,"price":price})


def price(request):
    if request.method == 'POST':
        quote = request.POST["quote"]
        quote = quote.upper()
        cypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote+"&tsyms=USD")
        cypto = json.loads(cypto_request.content)
        return render(request,"price.html",{"quote":quote,"cypto":cypto})
    else:
        doerror = "no much cypto"
        return render(request,"price.html",{"doerror":doerror})