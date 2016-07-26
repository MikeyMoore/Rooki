from django.shortcuts import render
from django.http import HttpResponse
# import img_process_runner
from img_process_runner import getAfterCoordinates
from notate_runner import run_opencv
# Create your views here.
def index(request):
    # getAfterCoordinates('../IMG_0141.jpg','../IMG_0142.jpg')
    run_opencv()
    # import ipdb; ipdb.set_trace()

    # return coordinates

    return HttpResponse("Hello, world. You're at the polls index.")
