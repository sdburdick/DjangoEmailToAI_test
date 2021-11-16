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
    
scott = User(email='fsdafasfrom-python-burdick.105456456@wright.edu');
scott.first_name = 'ScottPy'
scott.last_name = 'BurdickPy'
scott.save()


for user in User.objects:
    print(user.email)
    
    
import sys
import getpass

if sys.stdin.isatty():
   print ("Login to email2ai.test@gmail.com")
   username = raw_input("Username: ")
   password = getpass.getpass("Password: ")
else:
   username = sys.stdin.readline().rstrip()
   password = sys.stdin.readline().rstrip()

print ("Username: [%s], password [%s]" % (username, password) )   
    
    
import poplib
from email import parser



pop_conn = poplib.POP3_SSL('pop.gmail.com', '995')
pop_conn.user("email2ai.test@gmail.com")
pop_conn.pass_("gggeampmnlhmtxaw")

number_of_messages = len(pop_conn.list()[1])

#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# list() function return all email list
resp, mails, octets = pop_conn.list()
print(mails)
# retrieve the newest email index number
index = len(mails)
# server.retr function can get the contents of the email with index variable value index number.
resp, lines, octets = pop_conn.retr(index)
# lines stores each line of the original text of the message
# so that you can get the original text of the entire message use the join function and lines variable. 
msg_content = b'\r\n'.join(lines).decode('utf-8')
# now parse out the email object.
msg = Parser().parsestr(msg_content)
# get email from, to, subject attribute value.
email_from = msg.get('From')
email_to = msg.get('To')
email_subject = msg.get('Subject')
print('From ' + email_from)
print('To ' + email_to)
print('Subject ' + email_subject)

class EmailContents(Document):
    subject = StringField()
    contents = StringField()
    
newmail = EmailContents(subject = email_subject)
newmail.save()
    

pop_conn.quit()
