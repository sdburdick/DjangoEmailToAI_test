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

    j = '  '
    k = '  '
    for email in Totality.emails.objects:
        if email.contentsE != None:
            k += email.contentsE + ' '
        if email.subject != None:
            j += email.subject + ' '
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
