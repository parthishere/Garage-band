from rest_framework import serializers

from portfolio.models import UserProfileModel, User
from friendship.models import Follow, Block


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = [
            'id',
            'user',
            'dob',
            'profession',
            'softwear',
            'about',
            'slug',
            'tags',
        ]
        read_only_fields = ['user', 'id', 'slug']


class ProfileCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

    def create(self, validated_data):
        user = super(ProfileCreateSerializer).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(ProfileCreateSerializer).update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user



class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = [
            'follower',
            'followee'
        ]

    def create(self, validated_data):
        follow = super(ProfileCreateSerializer).create(validated_data)
        follow(follower=request.user)
        user.save()
        return user
