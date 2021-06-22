from django.views.generic import TemplateView, CreateView, ListView
from . import models


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class JokesPageView(TemplateView):
    template_name = 'pages/jokes.html'


class JokesPageView(ListView):
    template_name = 'pages/jokes.html'
    model = models.Joke


class JokeCreateView(CreateView):
    template_name = 'pages/create_joke.html'
    model = models.Joke
    fields = ['joke_text', 'author']