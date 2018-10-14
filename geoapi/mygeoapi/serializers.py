from rest_framework import serializers
from django.contrib.auth.models import User, Group
from mygeoapi.models import School
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class SchoolSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = School
        geo_field = 'location'
        auto_bbox = True

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'name', 'county', 'enrollment', 'location', 'electricity_availability', 'emmis_code')
