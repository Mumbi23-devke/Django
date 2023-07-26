from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False)
    age = models.IntegerField(blank=False)
    gender = models.CharField(blank=False, max_length=10)


def __str__(self):
    return self.name
