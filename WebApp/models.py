from django.conf import settings
from django.db import models
from django.utils import timezone

class Dish(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    r_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    tag = models.TextField(max_length=100)
    ingredients = models.TextField()
    imageUrl = models.TextField()
    direction = models.TextField()
    last_update = models.DateTimeField(default=timezone.now)
    timeToCook = models.IntegerField()

    def post(self):
        self.save()

    def __str__(self):
        return self.title
    
