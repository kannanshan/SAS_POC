from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def loadInitialSASPage(request):
   # return HttpResponse("Hello World!")
    print "INITIAL PAGE"
    return render_to_response("Templates/home.html")

def getSimilarTickets(request):
	print "Similar tickets page"
	ticketID = request.POST.get('jsonText')
	print ticketID
	similarTickets = getSimilarTicketsFromMLEngine(ticketID)
	return HttpResponse("Similar Ticket Id's")

def getSimilarTicketsFromMLEngine(ticketID):
	similarTickets = []
	similarTickets.append("1")
	similarTickets.append("2")
	similarTickets.append("3")
	return similarTickets
