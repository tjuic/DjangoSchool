from django.shortcuts import render #pull from template
from django.http import HttpResponse    #print text

def HomePage(request):
    #return HttpResponse('<h1>Hello My Name</h1>')
    return render(request, 'school/home.html')

def AboutPage(request):
    return render(request, 'school/about.html')

def ContactUs(request):
    return render(request, 'school/contact.html')