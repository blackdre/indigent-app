from rest_framework import generics  # for generic view in browser
# database models from community_data/models.py
from .models import Person, Residence
from .serializers import ResidenceSerializer, PersonSerializer  # serialized data

# List of people


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# Single person details view


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# List of houses


class ResidenceList(generics.ListCreateAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer

# Single house listing


class ResidenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer
