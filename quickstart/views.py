from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from quickstart.serializers import UserSerializer, GroupSerializar

class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allow users be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allow groups be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializar
    permission_classes = [permissions.IsAuthenticated]