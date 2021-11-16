# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:31:05 2021

@author: Email2AI
"""

from mongoengine import *
#open the database (already running0)
connect("testE")


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    
scott = User(email='fsdafasfrom-python-burdick.10@wright.edu');
scott.first_name = 'ScottPy'
scott.last_name = 'BurdickPy'
scott.save()


for user in User.objects:
    print(user.email)
