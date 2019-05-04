from django.shortcuts import render, HttpResponse
import requests
import json
import datetime
from .models import NasaData
from .models import NasaWallpaper

def home(request):
    data = dict()
    parsedData = []
    if not (NasaWallpaper.objects.filter(DATE=datetime.date.today()).exists()):
        if request.method == 'GET':
            req = requests.get('https://api.nasa.gov/planetary/apod?api_key=iuhNgzwxe8bTEazDdALqx8yd5PIZpQ9XGhX5yVkt')
            jsonList = [json.loads(req.content.decode('utf-8'))]

            for background in jsonList:
                IMG_SRC = background['url']

                HDURL = background['hdurl']

                TITLE = background['title']

                DATE = background['date']

            nasa_data = NasaWallpaper(IMG_SRC=IMG_SRC,
                                      HDURL=HDURL,
                                      TITLE=TITLE,
                                      DATE=DATE)
            nasa_data.save()

        else:
            data['wallpapers'] = NasaWallpaper.objects.latest()
            return render(request, 'home.html', data)

    data['wallpapers'] = NasaWallpaper.objects.filter(DATE=datetime.date.today())
    return render(request, 'home.html', data)


def picsviewer(request, earth_date, camera_name):
    data = dict()
    parsedData = []

    date = datetime.datetime.strptime(earth_date, '%Y-%m-%d')
    if date >= datetime.datetime.now():
        earth_date = str(datetime.datetime.today() - datetime.timedelta(days=1))[:10]

    if not (NasaData.objects.filter(EARTH_DATE=earth_date).exists()):
        if request.method == 'GET':
            api_key = "&api_key=pEqx0KfvYk6o3MbDGmFMxgMvb4rFhndc2eXyZoqx"
            req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + api_key
            response = requests.get(req)
            todo = json.loads(response.text)

            for pics in todo['photos']:
                EARTH_DATE = pics['earth_date']
                CAMERA_NAME = pics['camera']['name']
                CAMERA_ID = pics['id']
                IMG_SRC = pics['img_src']

                if not (NasaData.objects.filter(IMG_SRC=pics['img_src']).exists()):
                    nasa_data = NasaData(CAMERA_ID=CAMERA_ID,
                                         CAMERA_NAME=CAMERA_NAME,
                                         EARTH_DATE=EARTH_DATE,
                                         IMG_SRC=IMG_SRC)
                    nasa_data.save()

        else:
            data['pics'] = NasaData.objects.latest()
            return render(request, 'home.html', data)

    data['pics'] = NasaData.objects.filter(EARTH_DATE=earth_date).filter(CAMERA_NAME=camera_name)
    print(data['pics'])
    return render(request, 'home.html', data)


def allpics(request, earth_date):
    data = dict()
    parsedData = []

    date = datetime.datetime.strptime(earth_date, '%Y-%m-%d')
    if date >= datetime.datetime.now():
        earth_date = str(datetime.datetime.today() - datetime.timedelta(days=1))[:10]

    if not (NasaData.objects.filter(EARTH_DATE=earth_date).exists()):
        if request.method == 'GET':
            api_key = "&api_key=pEqx0KfvYk6o3MbDGmFMxgMvb4rFhndc2eXyZoqx"
            req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + api_key
            response = requests.get(req)
            todo = json.loads(response.text)

            for pics in todo['photos']:
                EARTH_DATE = pics['earth_date']
                CAMERA_NAME = pics['camera']['name']
                CAMERA_ID = pics['id']
                IMG_SRC = pics['img_src']

                if not (NasaData.objects.filter(IMG_SRC=pics['img_src']).exists()):
                    nasa_data = NasaData(CAMERA_ID=CAMERA_ID,
                                         CAMERA_NAME=CAMERA_NAME,
                                         EARTH_DATE=EARTH_DATE,
                                         IMG_SRC=IMG_SRC)
                    nasa_data.save()

        else:
            data['pics'] = NasaData.objects.latest()
            return render(request, 'home.html', data)

    data['pics'] = NasaData.objects.filter(EARTH_DATE=earth_date)
    print(data['pics'])
    return render(request, 'home.html', data)

def panelfilter(request, id):
    data=[]
    URL= NasaData.objects.values_list('IMG_SRC', flat=True).get(CAMERA_ID=id)
    data.append(URL)
    data.append(URL)
    return render(request, 'home.html', {'panelfilters' : data})