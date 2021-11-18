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
    
    leftS = ''
    centerS = ''
    rightS = ''
    leftC = ''
    centerC = ''
    rightC = ''
    pxLs = ''  #project X left/center/right subject/contents
    pxCs = ''
    pxRs = ''
    pxLc = ''
    pxCc = ''
    pxRc = ''
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
        
    for item in Totality.projX.objects:
        if not pxLc:
            if email.contentsE != None:
                split = item.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                pxLc = split[0] + ' '
            if email.subject != None:
                split = item.subject.split('\n')
                pxLs = split[0] + ' ' 
        elif not pxCc:
            if email.contentsE != None:
                split = item.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                pxCc = split[0] + ' '
            if email.subject != None:
                split = item.subject.split('\n')
                pxCs = split[0] + ' ' 
        elif not pxRc:
            if email.contentsE != None:
                split = item.contentsE.split("Sent") #this line just shortcuts to removing all the html from the email and just shows the contents when sent from windows mail
                pxRc = split[0] + ' '
            if email.subject != None:
                split = item.subject.split('\n')
                pxRs = split[0] + ' ' 

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'leftS': leftS,
            'leftC': leftC,
            'centerS': centerS,
            'centerC': centerC,
            'rightS': rightS,
            'rightC': rightC,
            'pxLs': pxLs, #project x left, center, right, subject, contents
            'pxCs': pxCs,
            'pxRs': pxRs,
            'pxLc': pxLc,
            'pxCc': pxCc,
            'pxRc': pxRc,
        }
    )

def contact(request):
    """Renders the contact page."""
    j = ''
    k = ''
    l = ''
    m = ''

    for user in Totality.userDb2.objects:
        if not j:
            j = user.email
            nj = user.first_name + ' ' + user.last_name
        elif not k:
            k = user.email
            nk = user.first_name + ' ' + user.last_name
        elif not l:
            l = user.email
            nl = user.first_name + ' ' + user.last_name
        elif not m:
            m = user.email
            nm = user.first_name + ' ' + user.last_name
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'name1': nj,
            'name2': nk,
            'name3': nl,
            'name4': nm,
            'message1': j,
            'message2': k,
            'message3': l,
            'message4': m,
            'year':datetime.now().year,
        }
    )

def about(request):
    j = ''
    k = ''
    l = ''
    m = ''

    for user in Totality.userDb2.objects:
        if not j:
            j = user.email
        elif not k:
            k = user.email
        elif not l:
            l = user.email
        elif not m:
            m = user.email
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message1': j,
            'message2': k,
            'message3': l,
            'message4': m,
            'year':datetime.now().year,
        }
    )
