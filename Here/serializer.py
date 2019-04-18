
from rest_framework import serializers
from .models import  Image,Profile


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('project', 'project_description', 'project_name')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'prof_picture', 'user_bio')

