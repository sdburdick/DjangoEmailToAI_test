"""
Definition of models.
"""

from django.db import models

# Create your models here.
import mongoengine
from mongoengine import *
DATABASE_NAME = 'testE'
mongoengine.connect(db=DATABASE_NAME)#, host=DATABASE_HOST, username=USERNAME, password=PASSWORD)

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'allow_inheritance': True}

class EmailContents(Document):
    subject = StringField()
    contents = StringField()

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()


    #uncomment to seed the database with our contact info
#scott = User(email='burdick.10@wright.edu');
#scott.first_name = 'Scott'
#scott.last_name = 'Burdick'
#scott.save()

#michael = User(email='celesti.2@wright.edu');
#michael.first_name = 'Michael'
#michael.last_name = 'Celesti'
#michael.save()

#daniel = User(email='chong.8@wright.edu');
#daniel.first_name = 'Daniel'
#daniel.last_name = 'Chong'
#daniel.save()

#john = User(email='garrett.115@wright.edu');
#john.first_name = 'Jonathon'
#john.last_name = 'Garrett'
#john.save()


class Totality(models.Model):
    userX = models.CharField(max_length = 100)
    #userDefault = scott
    #userdB = mongoengine.User.michael
    userDb2 = User
    emails = EmailContents


for post in Post.objects:
    print(post.title)

