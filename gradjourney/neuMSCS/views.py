from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


# Create your views here.
def neu_mscs_List(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'neuMSCS/neumscs_list.html', {'articles':articles})

def article_detail(request,slug):
    #return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'neuMSCS/article_detail.html', {'article':article})
