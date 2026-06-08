from rest_framework import serializers
from .models import Film


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'release_year', 'rating', 'is_hit']

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'