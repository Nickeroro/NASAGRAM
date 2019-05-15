from django.shortcuts import render, HttpResponse
import requests
import json
import datetime
import urllib.request
import os
from django.conf import settings
from .models import NasaData
from .models import NasaWallpaper
import sys
sys.path.append(settings.STATIC_HOME + 'picturesfilters/')
from color_transfer import color_transfer
from other_filters import *
import cv2


def home(request):
    data = dict()
    parsedData = []
    if not (NasaWallpaper.objects.filter(DATE=datetime.date.today()).exists()):
        if request.method == 'GET':
            req = requests.get("https://api.nasa.gov/planetary/apod?" + settings.API_NASA)
            jsonList = [json.loads(req.content.decode('utf-8'))]

            for background in jsonList:
                try:
                    IMG_SRC = background['url']
                except :
                    IMG_SRC = 'https://apod.nasa.gov/apod/image/1905/20190202tezel.jpg'

                try : 
                    HDURL = background['hdurl']
                except :
                    HDURL = 'https://apod.nasa.gov/apod/image/1905/20190202tezel.jpg'

                try :    
                    TITLE = background['title']
                except : 
                    TITLE = ''

                try :
                    DATE = background['date']
                except : 
                    DATE = datetime.date.today()

            try : 
                nasa_data = NasaWallpaper(IMG_SRC=IMG_SRC,
                                          HDURL=HDURL,
                                          TITLE=TITLE,
                                          DATE=DATE)


            except :
                nasa_data = NasaWallpaper(IMG_SRC='https://apod.nasa.gov/apod/image/1905/20190202tezel.jpg',
                                          HDURL='https://apod.nasa.gov/apod/image/1905/20190202tezel.jpg',
                                          TITLE='',
                                          DATE=datetime.date.today())

            finally : 
                nasa_data.save()

        else:
            data['wallpapers'] = NasaWallpaper.objects.latest()
            return render(request, 'home.html', data)

    data['wallpapers'] = NasaWallpaper.objects.filter(DATE=datetime.date.today())
    return render(request, 'home.html', data)


def picsviewerwithcamera(request, earth_date, camera_name):
    data = dict()
    parsedData = []

    date = datetime.datetime.strptime(earth_date, '%Y-%m-%d')
    if date >= datetime.datetime.now():
        earth_date = str(datetime.datetime.today() - datetime.timedelta(days=1))[:10]

    if not (NasaData.objects.filter(EARTH_DATE=earth_date).exists()):
        if request.method == 'GET':

            req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + '&' + settings.API_NASA
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
    return render(request, 'home.html', data)

def picsvieweronlycamera(request, camera_name):
    data = dict()
    data['pics'] = NasaData.objects.filter(CAMERA_NAME=camera_name)
    return render(request, 'home.html', data)

def picsviewerwithdate(request, earth_date):
    data = dict()
    parsedData = []

    date = datetime.datetime.strptime(earth_date, '%Y-%m-%d')
    if date >= datetime.datetime.now():
        earth_date = str(datetime.datetime.today() - datetime.timedelta(days=1))[:10]

    if not (NasaData.objects.filter(EARTH_DATE=earth_date).exists()):
        if request.method == 'GET':
            api_key = "&api_key=pEqx0KfvYk6o3MbDGmFMxgMvb4rFhndc2eXyZoqx"
            req = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=" + earth_date + '&' + api_key
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
    directory = settings.STATIC_HOME + 'picturesfilters/' + id + '/'

    if not os.path.exists(directory):
        os.makedirs(directory)

        URL = NasaData.objects.values_list('IMG_SRC', flat=True).get(CAMERA_ID=id)
        link = directory + 'source.jpg'
        urllib.request.urlretrieve(URL, link)

    target_ct = cv2.imread(settings.STATIC_HOME + 'picturesfilters/' + id + '/source.jpg')

    source_ct_orange = cv2.imread(settings.STATIC_HOME + 'picturesfilters/color_transfer/source_orange.jpg')
    transfer_orange = color_transfer(source_ct_orange, target_ct)
    cv2.imwrite(settings.STATIC_HOME + 'picturesfilters/' + id + '/output_ct_orange.jpg', transfer_orange)

    source_ct_polaroid = cv2.imread(settings.STATIC_HOME + 'picturesfilters/color_transfer/source_polaroid.jpg')
    transfer_polaroid = color_transfer(source_ct_polaroid, target_ct)
    cv2.imwrite(settings.STATIC_HOME + 'picturesfilters/' + id + '/output_ct_polaroid.jpg', transfer_polaroid)

    target_edge_detection = edge_detection(target_ct)
    cv2.imwrite(settings.STATIC_HOME + 'picturesfilters/' + id + '/output_edge_detection.jpg', target_edge_detection)

    target_fft = fourier_transform(target_ct)
    cv2.imwrite(settings.STATIC_HOME + 'picturesfilters/' + id + '/output_fft.jpg', target_fft)

    data.append(id + '/source.jpg')
    data.append(id + '/output_ct_orange.jpg')
    data.append(id + '/output_ct_polaroid.jpg')
    data.append(id + '/output_edge_detection.jpg')
    data.append(id + '/output_fft.jpg')
    
    return render(request, 'home.html', {'panelfilters' : data})
