#I have created this file- Sayali
from collections import OrderedDict
from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def analyze(request):
    #Get the Text
    djtext =request.POST.get('text', 'default')
    print(djtext)

    #check with checkbox is on
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed


    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new Line', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcounter == "on"):
        # analyzed = 0
        count=0
        for char in djtext:
            if(char.isalpha()):
                count+=1

        analyzed= djtext+"\nThe Count Of Characters Are:"+str(count)
        params = {'purpose': 'Count The characters', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            # if djtext[index]==" " and djtext[index+1]==" ":
            #     pass
            # else:
            #     analyzed = analyzed + char
            # Or
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcounter!="on"):
        return HttpResponse("Please Select Any Operation And Try Again..")

    return render(request, 'analyze.html', params)







