from rest_framework import serializers
from .models import Movie, Rating, Comment
from drf_writable_nested import WritableNestedModelSerializer
from django.db.models import Count


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('Source', 'Value')


class MovieSerializer(WritableNestedModelSerializer):
    Ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'




class MoviesTopSerializator(serializers.ModelSerializer):

    movie_id = serializers.IntegerField(source='id', read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    rank = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'total_comments', 'rank')
    


    
