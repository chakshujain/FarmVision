from django.shortcuts import render,HttpResponse
import requests
from .models import Crop,FarmersQuery
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .ml.ml_algo import * 

w_key = "4c14c1a61b22493a98a122059191012"
latitude = 0
longitude = 0
# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        startdate = "2009-07-22"
        enddate = "2009-09-22"
        # response = requests.get('http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=' + str(w_key) + '&q='+ str(latitude) + ',' + str(longitude) + '&fx24=yes&date=' + startdate + '&tp=24&enddate='+ enddate + '&mca=yes&format=json')
        response = requests.get('http://api.worldweatheronline.com/premium/v1/weather.ashx?key=' + str(w_key) + '&q='+ str(latitude) + ',' + str(longitude) + '&fx=no&mca=yes&cc=no&format=json')

        rainfall = response.json()['data']['ClimateAverages'][0]['month']
        rainfall_values = []
        temp = []
        
        for i in range(0,12):
            rainfall_values.append(float(rainfall[i]['avgDailyRainfall'])*30)
            temperature = (float(rainfall[i]['avgMinTemp']) + float(rainfall[i]['absMaxTemp']))/2
            temp.append(temperature)

        print(temp)
        print(setData(rainfall_values,temp,"Haryana"))
    
        
        # currentMonth = str(datetime.now().month)
        # currentDate = str(datetime.now().date)
        # print(currentMonth)
        # if int(currentDate) >15:
        #     currentMonth = currentMonth + 1
        # else:
        #     currentMonth = currentMonth
        #     print(currentMonth)
        #     print(type(currentMonth))

        


        

        
       

    return render(request,"home.html",context)
@csrf_exempt
def example(request):
    global latitude
    global longitude
    latitude = request.POST['lat']
    longitude = request.POST['long']
    return HttpResponse("OK")
