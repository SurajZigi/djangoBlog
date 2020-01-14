from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_psoted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    #dunder str method (__)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-details', kwargs={'pk': self.pk})




