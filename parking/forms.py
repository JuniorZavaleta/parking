from django import forms

from parking.models import Ticket, Vehicle, VehicleType


class RegisterTicketForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(Vehicle.objects.all(), widget=forms.Select)

    amount = forms.Field(widget=forms.TextInput({
        'readonly': 'true'
    }))

    class Meta:
        model = Ticket
        fields = ['vehicle', 'paid', 'amount']
        exclude = ['departure_time', 'entry_time']
