from rest_framework.viewsets import ModelViewSet

from cms.models import User
from cms.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer