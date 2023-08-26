from cms.models import TumorDetection
from rest_framework import serializers
class TumorDetectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TumorDetection
        fields = '__all__'