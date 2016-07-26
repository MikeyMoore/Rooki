from django.shortcuts import render
from django.http import HttpResponse
# import img_process_runner
from img_process_runner import getAfterCoordinates
from notate_runner import run_opencv
# Create your views here.
def index(request):
    # getAfterCoordinates('../IMG_0141.jpg','../IMG_0142.jpg')

   
    notation = run_opencv('../../IMG_0322.jpg','../../IMG_0323.jpg')


    # import ipdb; ipdb.set_trace()

    # return coordinates

   
    return HttpResponse(notation)

# def post(request):

# 	return HttpResponse("this is a post request")
