from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    phone = models.IntegerField(default=1)
    email = models.EmailField(unique=True, blank=False)
    age = models.IntegerField(blank=False)
    country = models.CharField(null=False, max_length=30, default=65)
    city = models.CharField(null=False, max_length=30, default=34)
    gender = models.CharField(blank=False, max_length=10)


def __str__(self):
    return self.name
