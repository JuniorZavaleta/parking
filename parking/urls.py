from django.conf.urls import url

from parking.views import IndexView, RegisterTicketView, VehicleView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^ticket/register$', RegisterTicketView.as_view(), name='ticket.register'),
    url(r'^vehicle/(?P<pk>\d+)$', VehicleView.as_view(), name='vehicle.data'),
]
