from django.db import models


class CustomUser(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=50)

