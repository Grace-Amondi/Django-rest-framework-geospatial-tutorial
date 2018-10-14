from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, SchoolSerializer
from .models import School
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'schools': reverse('schools-list', request=request, format=format),
    })

class UserViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows users to be viewed or edited.
       """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows group to be viewed or edited.
       """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    distance_filter_field = 'geometry'
    filter_backends = (DistanceToPointFilter,)
    bbox_filter_include_overlapping = True
