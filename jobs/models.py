
from django.db import models

from account.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, primary_key=True)
    parent = models.ForeignKey('self',
                               related_name='children',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class JobImage(models.Model):
    job = models.ForeignKey(Job, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs', null=True, blank=True)


class Resume(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100, blank=True)
        description = models.TextField()




class ResReply(models.Model):
        resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
        name = models.CharField(max_length=100, blank=True)


class JobReply(models.Model):
      resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
      job = models.ForeignKey(Job, on_delete = models.CASCADE)
