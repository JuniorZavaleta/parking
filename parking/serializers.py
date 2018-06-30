from rest_framework import serializers

from parking.models import Ticket, Vehicle, VehicleType, Client


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('name', 'payment_per_night')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'nickname', 'document_number', 'is_member', 'is_banned')


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ('pk', 'vehicle_type', 'license_plate', 'is_exonerated')


class VehicleVerboseSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ('vehicle_type', 'license_plate', 'client', 'is_exonerated')


class TicketSerializer(serializers.ModelSerializer):
    vehicle = VehicleVerboseSerializer(read_only=True)
    entry_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    def create(self, validated_data):
        validated_data['vehicle_id'] = self.initial_data['vehicle_id']
        ticket = Ticket.objects.create(**validated_data)
        return ticket

    class Meta:
        model = Ticket
        fields = ('pk', 'vehicle', 'watchman', 'entry_time', 'departure_time', 'amount', 'paid', 'vehicle_id')
