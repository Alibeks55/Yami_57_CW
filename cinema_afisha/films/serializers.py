from rest_framework import serializers
from .models import Film, Director, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'fio', 'birthday' ]


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genres = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'release_year', 'rating', 'is_hit', 'director', 'genres', 'reviews']
        #depth = 1

    def get_genres(self, film):
         return film.gener_list


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'