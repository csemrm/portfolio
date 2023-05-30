from django.contrib import admin
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email


class Project(models.Model):
    title = models.CharField(max_length=255)
    summery = models.TextField(max_length=1000)
    url = models.URLField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

    @admin.display(
        boolean=None,
        ordering="id",
        description="# of screen uploaded",
    )
    def number_screen_uploaded(self):
        return ProjectImage.objects.filter(project=self).count()


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
