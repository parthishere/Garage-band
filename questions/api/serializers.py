from rest_framework import serializers
from questions.models import Questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['user','question','image','like','dislike','like_count','dislike_count','draft','saved','tags']
        read_only_fields = ['slug','time']


    def update(self, instance, validated_data):

        instance.user = validated_data.get('user', instance.user)
        instance.image = validated_data.get('image', instance.image)
        instance.like = validated_data.get('like', instance.like)
        instance.dislike = validated_data.get('dislike', instance.dislike)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.saved = validated_data.get('saved', instance.saved)
        instance.tags = validated_data.get('tags', instance.tags)

        instance.save()
        return instance
class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'user',
            'time',
            'question',
            'image',
            'tags',
            'like',
            'dislike',
            'draft',
            'saved',

        ]
        def __init__(self, user, like , dislike):
            self.user = request.user
            self.like = request.like
            self.dislike = request.dislike
            return self.user

        def create(self, validated_data):
            return Questions.objects.create(**validated_data)

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'user',
            'time',
            'question',
            'image',
            'tags',
            'like',
            'dislike',
            'like_count',
            'dislike_count'
        ]

class UpvoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
        'user',
        'question',
        'image',
        'like',
        'like_count',
        'time',
        'tag'
        ]
class QuestionListDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'user',
            'time',
            'question',
            'image',
            'tags',
            'like',
            'dislike',
            'like_count',
            'dislike_count'
        ]
class QuestionListSavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'user',
            'time',
            'question',
            'image',
            'tags',
            'like_count',
            'dislike_count'
        ]
