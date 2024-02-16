from django.shortcuts import render
from api import address
from private_file import key
import json
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    # print(request.POST)
    # print(request.POST["address1"])
    # print(request.POST["address2"])
    # if request.method == "POST":
    #     address1 = request.POST["address1"]
    #     address2 = request.POST["address2"]
    #     # address1 = "서울시"
    #     # address2 = "마포구"
    #     keyword = "웨딩메이크업"
    #     data = address.search(address1, address2, keyword)
    # else: 
    #     data = address.search()
    # context = {
    #     "data" : data[:5]
    # }


    return render(request, "index.html")

def map(request):
    data = address.search()
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    a = geolocoder.reverse("37.5424411 126.9433486")    
    context = {
        "map_key" : key.kakao_map_key,
        "data" : json.dumps(data), 
        "position" : a
    }
    return render(request, "map.html", context)