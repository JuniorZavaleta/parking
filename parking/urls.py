from django.conf.urls import url

from parking.views import IndexView, RegisterTicketView, VehicleView, TicketListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^ticket/register$', RegisterTicketView.as_view(), name='ticket.register'),
    url(r'^vehicle$', VehicleView.as_view(), name='vehicle.list'),
    url(r'^tickets/today$', TicketListView.as_view(), name='ticket.today'),
]
