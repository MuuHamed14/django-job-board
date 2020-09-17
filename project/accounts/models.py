from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile', null=True, blank=True)
    number_phone = models.CharField(max_length=15)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s ' % self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
