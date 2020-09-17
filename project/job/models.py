from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from django.contrib.auth.models import User


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return 'jobs/%s.%s' % (instance.id, extension)


class Job(models.Model):
    objects = None
    JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    )
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    like = models.ManyToManyField(User,blank=True)
    location = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    facebook = models.CharField(max_length=500,null=True,blank=True)
    instagram = models.CharField(max_length=500,null=True,blank=True)
    google = models.CharField(max_length=500,null=True,blank=True)
    twitter = models.CharField(max_length=500,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    class meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    class meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name = _('Apply')
        verbose_name_plural = _('Applies')

    def __str__(self):
        return self.name
