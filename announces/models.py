from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Announce(models.Model):
    categories =[
        ('tanks', 'Танки'),
        ('hills', 'Хилы'),
        ('dd', 'ДД')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=12, choices=categories, default='tanks')
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(blank=True)
    file = models.FileField(blank=True)


class Reply(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    replier = models.ForeignKey(User, on_delete=models.CASCADE)