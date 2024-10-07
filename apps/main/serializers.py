from .models import Collections, Services, Contacts, About, Projects, Maintitle
from rest_framework import serializers


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class MaintitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintitle
        fields = "__all__"
