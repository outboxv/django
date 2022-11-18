from rest_framework import serializers
from base.models import Stores

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stores
        fields='__all__'