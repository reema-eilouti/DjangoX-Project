from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Joke(models.Model):
    joke_text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('jokes')
    

# Create your models here.
