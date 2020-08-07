from rest_framework import serializers
from linkra_app.models import Linkra
from .models import Questions

class LinkraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
