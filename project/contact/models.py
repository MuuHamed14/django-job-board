from django.db import models


class Info(models.Model):
    objects = None
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email
