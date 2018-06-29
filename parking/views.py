from django.utils import timezone
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from parking.models import Vehicle, Ticket
from parking.serializers import TicketSerializer, VehicleSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class VehicleView(APIView):

    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)


class TicketListView(APIView):

    def get(self, request, format=None):
        today = timezone.now()
        yesterday = today - timezone.timedelta(days=1)
        tickets = Ticket.objects.filter(entry_time__range=[yesterday, today])
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
