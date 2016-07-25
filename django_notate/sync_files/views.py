from django.shortcuts import render
from django.http import HttpResponse
from img_process_runner import getCoordinates
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # import ipdb; ipdb.set_trace()
    coordinates = getCoordinates('../IMG_0141.jpg','../IMG_0142.jpg')

    return coordinates
