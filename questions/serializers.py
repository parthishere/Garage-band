from rest_framework import serializers
from linkra_app.models import Linkra

class LinkraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
