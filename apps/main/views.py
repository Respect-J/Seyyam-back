from .models import Collections, Services, Contacts, About, Projects, Maintitle
from .serializers import CollectionsSerializer, ServicesSerializer, ContactsSerializer, BannersSerializer, \
    ProjectsSerializer, MaintitleSerializer
from rest_framework import generics


class CollectionsListView(generics.ListAPIView):
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer


class ServicesListView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ContactsListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ProjectsListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class BannersListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = BannersSerializer


class MaintitleListView(generics.ListAPIView):
    queryset = Maintitle.objects.all()
    serializer_class = MaintitleSerializer
