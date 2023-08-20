from rest_framework.serializers import HyperlinkedModelSerializer
from cms.models import User

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']