from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to="profile_images", default="default.png")
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# creating blog models
class BlogPost(models.Model):
    image = models.ImageField(upload_to="Blog-Images")
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(null=True)
    author1 = models.CharField(max_length=100)

    class meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title


# creating contact models
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True)
    date_send = models.DateTimeField(auto_now_add=True)

    odering = [
        "-date_send",
    ]

    def __str__(self):
        return self.name


# creating matches model
class UpcomingMatches(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    match_date = models.DateField()
    time = models.TextField(null=True)

    def __str__(self):
        return self.team1
    
class Results(models.Model):
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200, default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    scores = models.IntegerField(null=True)
    score2 = models.IntegerField(null=True, default=False)
    competition_name = models.TextField(default=False)
    
    def __str__(self):
        return self.competition_name
    
#creating a model for comment
class Comment(models.Model):
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(default=True)
    updated = models.DateTimeField(default=False)
    
    def __str__(self):
        return self.comment