from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creating database tables.

class Topic(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) 
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True) #cant be blank
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now = True) #take snap shot everytime it is saved
    created = models.DateTimeField(auto_now_add = True) #take snap shot only when it is created

    def __str__(self):
        return self.name

#FIRST ITEM IN THE LIST IS PRIORTIZED
class Meta:
    ordering = ['-updated', '-created']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    room = models.ForeignKey(Room, on_delete = models.CASCADE)  #if room is deleted all the messages are deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True) #take snap shot everytime it is saved
    created = models.DateTimeField(auto_now_add = True) #take snap shot only when it is created

    class Meta:
        ordering = ['-updated', '-created']

def __str__(self):
     return self.body[0:50] #limit to 50 words