from django.shortcuts import render, HttpResponse
import requests
import json


def home(request):
    parsedData = []
    if request.method == 'GET':
        req = requests.get('https://api.nasa.gov/planetary/apod?api_key=iuhNgzwxe8bTEazDdALqx8yd5PIZpQ9XGhX5yVkt')
        jsonList = []
        jsonList.append(json.loads(req.content.decode('utf-8')))
        nasaData = {}
        for background in jsonList:
            nasaData['url'] = background['url']
            nasaData['hdurl'] = background['hdurl']
            nasaData['title'] = background['title']
        parsedData.append(nasaData)
    return render(request, 'home.html', {'background': parsedData})


def picsviewer_old(request, earth_date, camera_name):
    parsedData = []
    print("ok")
    if request.method == 'GET':
        api_key = "&api_key=pEqx0KfvYk6o3MbDGmFMxgMvb4rFhndc2eXyZoqx"
        req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + api_key
        jsonList = []
        jsonList.append(json.loads(req.content.decode('utf-8')))
        nasaData = {}
        for pics in jsonList:
            nasaData['earth_date'] = pics['earth_date']
            nasaData['camera_name'] = pics['camera']['name']
            nasaData['id'] = pics['id']
            nasaData['img_src'] = pics['img_src']

            parsedData.append(nasaData)
        return render(request, 'home.html', {'pics': parsedData})
    
def picsviewer(request, earth_date, camera_name):
    parsedData = []

    if request.method == 'GET':
        api_key = "&api_key=pEqx0KfvYk6o3MbDGmFMxgMvb4rFhndc2eXyZoqx"
        req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + api_key
        response = requests.get(req)
        todo = json.loads(response.text)
        nasaData = {}

        for pics in todo['photos']:
            EARTH_DATE = pics['earth_date']
            nasaData['earth_date'] = pics['earth_date']

            CAMERA_NAME = pics['camera']['name']
            nasaData['camera_name'] = pics['camera']['name']

            CAMERA_ID = pics['id']
            nasaData['id'] = pics['id']

            IMG_SRC = pics['img_src']
            nasaData['img_src'] = pics['img_src']
            buffer = CAMERA_ID
            parsedData.append(nasaData)

            if NasaData.objects.filter(CAMERA_ID=buffer).exists():
                print("Object already exists in DataBase, don't save anything")
            else:
                nasa_data = NasaData(CAMERA_ID=CAMERA_ID,
                                     CAMERA_NAME=CAMERA_NAME,
                                     EARTH_DATE=EARTH_DATE,
                                     IMG_SRC=IMG_SRC)
                nasa_data.save()


        return render(request, 'home.html', {'pics': parsedData})    
