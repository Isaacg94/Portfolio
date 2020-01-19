from django.db import models
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    profile_pic = ImageField(blank=True, manual_crop='1080x1080')
    bio = HTMLField()
    email = models.EmailField()

class Tags(models.Model):
    name = models.CharField(max_length=30)

class Tech(models.Model):
    name = models.CharField(max_length=60)

class Skill(models.Model):
    skill = models.CharField(max_length=60)
    about_skill = models.TextField()

class Link(models.Model):
    site_title = models.CharField(max_length=30)
    site_url = models.URLField(max_length=250)


class Blog(models.Model):
    blog_title = models.CharField(max_length=60)
    blog_editor = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_post = HTMLField()
    blog_thumbnail = ImageField(manual_crop = '1920x1080')
    blog_tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)

class Projects(models.Model):
    project_title = models.CharField(max_length=60)
    project_description = models.TextField()
    project_thumbnail = ImageField(manual_crop = '1920x1080')
    tech_used = models.ManyToManyField(Tech)
    live_site = models.URLField(max_length=250) 

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()