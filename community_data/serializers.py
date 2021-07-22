from rest_framework import serializers
from .models import Person, Residence


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Person


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Residence
