from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    img = models.ImageField(upload_to='media/')
    created_by = models.ForeignKey(User, null=True,blank=True,related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
