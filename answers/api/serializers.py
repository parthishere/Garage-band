from rest_framework import serializers
from answers.models import Answers

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['user','question','image','like','dislike','like_count','dislike_count']
        read_only_fields = ['slug','time']


    def update(self, instance, validated_data):

        instance.user = validated_data.get('user', instance.user)
        instance.image = validated_data.get('image', instance.image)
        instance.like = validated_data.get('like', instance.like)
        instance.dislike = validated_data.get('dislike', instance.dislike)
        instance.tags = validated_data.get('tags', instance.tags)

        instance.save()
        return instance
class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = [
            'user',
            'time',
            'question',
            'image',
            'like',
            'dislike',

        ]
        def __init__(self, user, like , dislike):
            self.user = request.user
            self.like = request.like
            self.dislike = request.dislike
            return self.user

        def create(self, validated_data):
            return Answers.objects.create(**validated_data)
