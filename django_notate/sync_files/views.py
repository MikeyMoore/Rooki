from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from notate_runner import run_opencv
from sync_files.models import Document
from sync_files.forms import DocumentForm
from list_moves import listMoves
from sync_files.models import Document, Notations
import sqlite3

# conn = sqlite3.connect("db.sqlite3", check_same_thread = False)
# c = conn.cursor()

def index(request):
	imageCount = Document.objects.count()
	# imageCount = c.execute('SELECT COUNT(*) FROM sync_files_document')

	# # this logic saves the single move in db, 
	indexFirst = Document.objects.first().id
	increaseIndex = indexFirst
	print increaseIndex

	for x in range(indexFirst,(indexFirst + imageCount)):
		if (Document.objects.count() != 1):
			# images should be ImageObject.first and ImageObject.second
			# notation = run_opencv('../../IMG_0322.jpg','../../IMG_0323.jpg')
			print increaseIndex
			imageFirst = Document.objects.get(id=increaseIndex)
			increaseIndex += 1
			
			print increaseIndex
			imageSecond = Document.objects.get(id=(increaseIndex))

			# imageFirst = c.execute('SELECT * FROM sync_files_document WHERE ID=(?)', [x])
			# imageSecond = c.execute('SELECT * FROM sync_files_document WHERE id=(?)', [x+1])
			notation = run_opencv(imageFirst.docfile.url, imageSecond.docfile.url)
			newNotation = Notations(name=notation)
			newNotation.save()
	# 		c.execute('INSERT INTO sync_files_notations VALUES (?,?)', [x, notation])
		# need logic to delete first image
	# 		c.execute('DELETE FROM sync_files_document WHERE ID=(?)', x)
			imageFirst.delete()

	# # grab each notation object from database => 
	# # one notation object should look something like: 
	# # 'f8Be8'
	# # ============
	# # NotationObjects.all

	notationIndexFirst = Notations.objects.first().id
	indexForNotation = notationIndexFirst
	finalNotation = ""
	moveWhite = ""
	moveBlack = ""
	whiteOrBlack = "white"
	# notationCount = c.execute('SELECT COUNT(*) FROM sync_files_notations')
	notationCount = Notations.objects.count()
	for y in range(notationIndexFirst,(notationIndexFirst + notationCount)):
		if (Notations.objects.count() != 0):
			# for x in range(0, 2):
			moveNumber = str(notationIndexFirst - (notationIndexFirst-1)) + ". "
			
			if(whiteOrBlack == "white" and Notations.objects.count() != 0):
	# 			# need to call NotateObject id=indexForNotation
	# 			moveWhite = c.execute('SELECT * FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				moveWhite = Notations.objects.get(id=indexForNotation)
	# 			# delete NotateObject
	# 			c.execute('DELETE FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				whiteOrBlack = "black"
				indexForNotation +=1
				print "indexForNotation"
				print indexForNotation
				print "moveWhite"
				print moveWhite
				finalNotation += str(moveNumber) + str(moveWhite)
				moveWhite.delete()
			elif(whiteOrBlack == "black" and Notations.objects.count() != 0):
	# 			# need to call NotateObject id=indexForNotation
	# 			moveBlack = " .. " + "black" + str(indexForNotation)
				moveBlack =  Notations.objects.get(id=indexForNotation)
	# 			# delete NotateObject
	# 			c.execute('DELETE FROM sync_files_notations WHERE ID=(?)', [str(indexForNotation)])
				whiteOrBlack = "white"
				indexForNotation +=1
				print "indexForNotation"
				print indexForNotation
				print "moveBlack"
				print moveBlack
				finalNotation += " .. " + str(moveBlack) + "\n"
				moveBlack.delete()




	#     # c.execute('SELECT COUNT(*) FROM sync_files_notations')
	#     # c.execute('SELECT COUNT(*) FROM sync_files_document')
	#     # imageCount = c.fetchone()
	#     # return HttpResponse(notation)
	return HttpResponse(finalNotation)

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
    # return HttpResponse("yippee")







