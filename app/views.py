"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from mongoengine import *
from .models import Totality
from mongoengine import *


def home(request):
    """Renders the home page."""
    #updaing to allow for three things to appear on the home page, so hard coding the blocks to three
    j = ''
    k = ''
    leftS = ''
    centerS = ''
    rightS = ''
    leftC = ''
    centerC = ''
    rightC = ''
    for email in Totality.emails.objects:
        if not leftC:
            if email.contentsE != None:
                split = email.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                leftC = split[0] + ' '
            if email.subject != None:
                split = email.subject.split('\n')
                leftS = split[0] + ' ' 
        elif not centerC:
            if email.contentsE != None:
                split = email.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                centerC = split[0] + ' '
            if email.subject != None:
                split = email.subject.split('\n')
                centerS = split[0] + ' ' 
        elif not rightC:
            if email.contentsE != None:
                split = email.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                rightC = split[0] + ' '
            if email.subject != None:
                split = email.subject.split('\n')
                rightS = split[0] + ' ' 
        if email.contentsE != None:
            split = email.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
            k += split[0] + ' '
        if email.subject != None:
            split = email.subject.split('\n')
            j += split[0] + ' ' 
        if (email.contentsE == None and email.subject == None):
            k += "bad data"
            j += "bad data"
    

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'subjects': j,
            'contents': k,
            'leftS': leftS,
            'leftC': leftC,
            'centerS': centerS,
            'centerC': centerC,
            'rightS': rightS,
            'rightC': rightC,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    j = '  '

    for user in Totality.userDb2.objects:
       j += user.email + ' '

    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message': 'Tryin to get data from python ' + j,
            'year':datetime.now().year,
        }
    )
