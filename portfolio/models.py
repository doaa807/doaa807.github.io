from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users/images/')
    job_title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='projects/images/')
    url = models.URLField(blank=True)
    tools = TaggableManager(blank=True)
    
    def __str__(self) -> str:
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=100)
    progress = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class SocialMediaAccount(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_media_accounts/icons/')
    
    def __str__(self) -> str:
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    file = models.FileField(upload_to='resume/files/')
    
    def __str__(self) -> str:
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='certificates/files/')
    url = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.title

class Gallary(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(max_length=1000,null=True, blank=True)
    image = models.ImageField(upload_to='gallary/images/')
    url = models.URLField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.title

class Taggable(models.Model):
    title = models.CharField(max_length=100)
    tags = TaggableManager(blank=True)
    
    def __str__(self) -> str:
        return self.title