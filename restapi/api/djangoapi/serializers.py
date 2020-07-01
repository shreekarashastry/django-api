from rest_framework import serializers
from api.models import apiModel

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = apiModel
        fields = ["name","phone",]