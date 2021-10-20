from django.contrib.auth.models import User
from django.db import models


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url
