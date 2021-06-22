from django.urls import path

from .views import HomePageView, AboutPageView, JokesPageView, JokeCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('jokes/', JokesPageView.as_view(), name='jokes'),
    path('create_joke', JokeCreateView.as_view(), name='create_joke'),
]
