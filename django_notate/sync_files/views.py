from django.shortcuts import render
from django.http import HttpResponse
# 
# from django.http import HttpResponseRedirect
# from forms import UploadFileForm
# 
# import img_process_runner
# from img_process_runner import getAfterCoordinates
from list_moves import listMoves

# Create your views here.
def index(request):




    notation = listMoves()


    
   
    return HttpResponse(notation)


# def post(request):

	# save a photo to db
	







