from cms.models import TumorDetection
from rest_framework import serializers


class TumorDetectionSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = TumorDetection
        exclude = ["trained", "detection_class"]
