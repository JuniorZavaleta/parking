import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, FormView

from parking.forms import RegisterTicketForm
from parking.models import VehicleType, Vehicle


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterTicketView(FormView):
    template_name = 'form.html'
    form_class = RegisterTicketForm
    success_url = '/'

    def form_valid(self, form):
        form.cleaned_data['entry_time'] = now()
        form.save()
        return super(RegisterTicketView, self).form_valid(form)


class VehicleView(TemplateView):

    def get(self, request, *args, **kwargs):
        vehicle = Vehicle.objects.get(pk=kwargs['pk'])
        data = {
            'license_plate': vehicle.license_plate,
            'amount': vehicle.vehicle_type.payment_per_night
        }
        return JsonResponse(data, safe=True)
