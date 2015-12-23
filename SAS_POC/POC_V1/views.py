from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import TicketDetails
# Create your views here.

def home(request):
  return render_to_response("Templates/home.html")

@csrf_exempt
def get_ticket_details(request):
  ticket_id = int(request.POST.get('ticket_id'))
  print ticket_id
  ticket_detail = TicketDetails.objects.get(id=ticket_id)
  html = render_to_string('Templates/ticket_details.html', {'ticket_detail': ticket_detail})
  return HttpResponse(html)

@csrf_exempt
def get_similar_tickets(request):
  ticket_id = int(request.POST.get('ticket_id'))
  similar_tickets = get_similar_tickets_from_ml_engine(ticket_id)
  similar_tickets = TicketDetails.objects.filter(id__in =similar_tickets)
  html = render_to_string('Templates/similar_ticket_details.html', {'similar_tickets': similar_tickets})
  return HttpResponse(html)

def get_similar_tickets_from_ml_engine(ticket_id):
	similarTickets = []
	similarTickets.append("1")
	similarTickets.append("2")
	similarTickets.append("3")
	return similarTickets
