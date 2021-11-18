# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:31:05 2021

@author: Email2AI
"""

from mongoengine import *
from emailParser import *
#open the database (already running0)
connect("testE")


user_email = "email2ai.test@gmail.com"
user_password ="gggeampmnlhmtxaw"

class EmailContents(Document):
    subject = StringField()
    contentsE = StringField()
class ProjX(Document):
    subject = StringField()
    contentsE = StringField()

#get_user_email_status(user_email, user_password)
    
count = get_user_email_index(user_email, user_password)
    
while (count):
    subject, content = get_email_by_index(user_email, user_password, count)
    if "ProjX" in subject:
        newmail = ProjX(subject = subject)
        newmail.contentsE = content
        newmail.save()
    elif "ProjectX" in subject:
        newmail = ProjX(subject = subject)
        newmail.contentsE = content
        newmail.save()
    else:
        newmail = EmailContents(subject = subject)
        newmail.contentsE = content
        newmail.save()
 
    count = count -1
    
close_pop3_server_connection()

    
   

