from django.http import HttpResponse

def homepage(request):
    return HttpResponse('homepage')

def about(request):
    return HttpResponse('about') #sending in a respnose with a string about
