from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def loadInitialSASPage(request):
   # return HttpResponse("Hello World!")
     return render_to_response("Templates/home.html")
