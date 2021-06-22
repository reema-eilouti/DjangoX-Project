from django.urls import path

from .views import HomePageView, AboutPageView, JokesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('jokes/', JokesPageView.as_view(), name='jokes'),
]
