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


def picsviewer(request, earth_date, camera_name):
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
