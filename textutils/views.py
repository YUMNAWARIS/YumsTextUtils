# created by YUMS

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # taking text from Users
    djtext = request.POST.get('text', 'default')

    # options selected by user
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    lower = request.POST.get('lower', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    # Removing Punctuations
    if removepunc == 'on':
        list_of_punctuation = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', "'", '"', '\\', ',', '<', '>', '.',
                               '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~']
        analyzedtxt = ""
        for char in djtext:
            if char not in list_of_punctuation:
                analyzedtxt += char
        djtext = analyzedtxt

    # For UpperCase
    if upper == 'on':
        analyzedtxt = ""
        for char in djtext:
            analyzedtxt += char.upper()
        djtext = analyzedtxt

    # For LowerCase
    if lower == 'on':
        analyzedtxt = ""
        for char in djtext:
            analyzedtxt += char.lower()
        djtext = analyzedtxt

    # Extra Space Remover
    if spaceremover == 'on':
        analyzedtxt = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzedtxt = analyzedtxt + char
        djtext = analyzedtxt

    # New line Remover
    if newlineremover == 'on':
        analyzedtxt = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzedtxt = analyzedtxt + char
        djtext = analyzedtxt

    # If no option is selected
    if (removepunc != 'on') and (upper != 'on') and (lower != 'on') and (spaceremover != 'on') and (
            charcount != 'on') and (newlineremover != 'on'):
        return HttpResponse("<h1>Error... No option is selected...! </h1>")

    # Sending Response
    param = {'analyzed': djtext}
    return render(request, 'analyze.html', param)
