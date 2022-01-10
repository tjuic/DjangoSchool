from django.shortcuts import render #pull from template
from django.http import HttpResponse    #print text
from .models import Score

def HomePage(request):
    #return HttpResponse('<h1>Hello My Name</h1>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(request):
    return render(request, 'school/contact.html')

def ShowScore(request):
    score = Score.objects.all() #from database named Score, all objects, calling from database function
    context = {'score':score}

    return render(request, 'school/showscore.html', context)