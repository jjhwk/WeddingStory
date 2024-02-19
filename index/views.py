from django.shortcuts import render
from api import address
from private_file import key
import json
from django.http import JsonResponse

# Create your views here.
def index(request):    

    return render(request, "test.html")

def map(request):
    data = address.search()
    # geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    # a = geolocoder.reverse("37.5424411 126.9433486") 
    if request.method == "POST":
        print(request.body)
        fetchData = json.loads(request.body)
        print(fetchData)
        x = fetchData["x"]
        y = fetchData["y"]
        
        hall = address.searchGeo(x,y,"웨딩홀")
        studio = address.searchGeo(x,y,"스튜디오")
        dress = address.searchGeo(x,y,"웨딩드레스")
        print(data)
        return JsonResponse({
                                "hall": hall,
                                "studio" : studio,
                                "dress" : dress})
    context = {
        "map_key" : key.kakao_map_key,
        "data" : json.dumps(data), 
        # "position" : a
    }
    return render(request, "map.html", context)