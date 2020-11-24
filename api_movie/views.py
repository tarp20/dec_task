from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import MovieSerializer, CommentSerializer, MoviesTopSerializator
from rest_framework import status
import requests
from django.http import Http404
from django.db.models import Count
import datetime
from django.db.models.expressions import F, Window
from django.db.models.functions.window import DenseRank
from django.http import HttpResponse
from .models import Movie, Comment






def welcome(request):
    return HttpResponse("Hello! I'm working ")




class MoviesView(APIView):

    def get(self, request):

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):

        if request.data.get('title', 'year'):
            title = request.data['title']
            year = request.data['title']
        else:
            return Response(data={'Error': 'You must provide title and year in POST method'})

        api_key = API_KEY
        url = f'http://www.omdbapi.com/?t={title}&type=movie&apikey={api_key}&y={year}'
        response = requests.get(url)
        if response.status_code == 200 and response.json()['Response'] == 'True':
            if not Movie.objects.filter(Title=response.json()['Title']).exists():
                serializer = MovieSerializer(data=response.json())
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(data={"Error": "Problem with serializing data from external API"},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                movie_from_database = Movie.objects.get(
                    Title=response.json()['Title'])
                movie_from_database_serialized = MovieSerializer(
                    movie_from_database)
                return Response(movie_from_database_serialized.data)
        else:
            return Response(data={"Error": "No movie with that title"},
                            status=status.HTTP_204_NO_CONTENT)


class MovieView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = serializer = MovieSerializer(
            movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentsView(APIView):

    def get(self, request):
        if request.data.get('movie_id'):
            movie = Movie.objects.filter(id=request.data.get('movie_id'))
            if movie.count() != 0:
                return Response(data={"Error": "We don't have movie of this ID in database."},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                comments = Comment.objects.filter(
                    movie_id=request.data['movie_id'])
                if comments.count() == 0:
                    return Response(data={'We dont have comments for this movie...yet'},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not (request.data.get("comment_text") and request.data.get("movie_id")):
            return Response(data={"Error": "Provide comment and movie_id in POST request"},
                            status=status.HTTP_400_BAD_REQUEST)
        if Movie.objects.filter(id=request.data["movie_id"]).exists():
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={"Error": "We don't have movie of this ID in database."},
                        status=status.HTTP_400_BAD_REQUEST)


class MoviesTop(ListAPIView):

    serializer_class = MoviesTopSerializator

    def get_queryset(self):

        movies = Movie.objects.all()
        dense_rank = Window(expression=DenseRank(), order_by=F('total_comments').desc())
        movies_sort = movies.annotate(total_comments=Count('Comments')).order_by('-total_comments').annotate(rank=dense_rank)
        
        return movies_sort

        if self.request.query_params:
            date_start = self.request.query_params.get('date_start')
            date_end = self.request.query_params.get('date_end')
            sorted_date_movies = movies_sort.filter(
                                    Comments__pub_date__gte = date_start,
                                    Comments__pub_date__lte = date_end)
            return sorted_date_movies
            





        
        

        
        
