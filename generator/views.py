from django.shortcuts import render
#added from the course
from django.http import HttpResponse
from html.parser import HTMLParser
import random
import string
# Create your views here.

''' 
the home.html file goes inside the /templates/generator folders that we created
to beautify the project structure.
render - passes an html response with file and other parameters like dicts
'''
def home(request):
    return render(request, 'generator/home.html')


'''
returns a basic html response , passes a string parameter
'''
def password(request):
    # generating a random password
    try:
        length = int(request.GET.get('length', 13))
    except ValueError:
        return render(request, 'generator/unavailableLength.html')

    if length > 13 or length < 6:
        return render(request, 'generator/unavailableLength.html')

    #returns a list of lowercase letters
    characterslist = list(string.ascii_lowercase)
    thepassword = ''

    #extend to upper case letters
    if request.GET.get('uppercase'):
        characterslist.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characterslist.extend(list('!@#$%^&*()?'))

    if request.GET.get('numbers'):
        characterslist.extend(list('0123456789'))

    for x in range(length):
        #random.choice - choose random list member every round
        thepassword += random.choice(characterslist)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')

