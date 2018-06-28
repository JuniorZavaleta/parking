import datetime

from django.http import JsonResponse, Http404
from django.utils.timezone import now
from django.views.generic import TemplateView, FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from parking.forms import RegisterTicketForm
from parking.models import VehicleType, Vehicle, Ticket
from parking.serializers import TicketSerializer, VehicleSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterTicketView(FormView):
    template_name = 'form.html'
    form_class = RegisterTicketForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return JsonResponse({}, status=200)


class VehicleView(APIView):

    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


class TicketListView(APIView):

    def get(self, request, format=None):
        today = datetime.date.today()
        # yesterday = today - datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=7)
        tickets = Ticket.objects.filter(entry_time__range=[yesterday, today])
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
