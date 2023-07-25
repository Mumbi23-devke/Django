from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=30, blank=False)
    age = models.IntegerField()
    email_address = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.fullname} {self.age} {self.email_address} {self.phone_number} {self.password}"


class Teacher(models.Model):
    name = models.CharField(max_length=30, blank=False)
    tscno = models.CharField(max_length=30, blank=False)
    subject = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f"{self.name} {self.tscno} {self.subject}"

