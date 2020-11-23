from django.urls import path
from .views import MoviesView, MovieView, CommentsView,MoviesTop


urlpatterns = [
    path('movies/', MoviesView.as_view(), name='MoviesView'),
    path('comments/', CommentsView.as_view(), name='CommentsView'),
    path('movies/<int:pk>/', MovieView.as_view(), name='MovieView'),
    path('movies/top',MoviesTop.as_view(),),
]
