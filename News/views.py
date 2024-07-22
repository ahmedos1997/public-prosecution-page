from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import models
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.utils.translation import activate, gettext as _
from django.urls import reverse
from . models import  News, Image, AboutProsecution, AttorneyGeneral
# Create your views here.



def main(request):
    last_news = News.objects.order_by('-date')[:1]
    news = News.objects.order_by('-date')[1:4]  # احصل على آخر خبرين باستخدام ترتيب تنازلي للتواريخ
    about_prosecution = AboutProsecution.objects.all()
    attorney_general = AttorneyGeneral.objects.order_by('-start_date')[:2]

    context = {
        'news':news,
        'last_news':last_news,
        'about_prosecution':about_prosecution,
        'attorney_general':attorney_general,
    }
    return render(request, 'page/main.html', context)


########## news################

def news(request):
    news = News.objects.order_by('-date')

    paginate_by = 4

    paginator = Paginator(news, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news':page_obj,
        'paginator':paginator,
        'page_obj':page_obj,

    }
    return render(request, 'page/news.html', context)


def news_view(request, id):
    news = News.objects.get(id=id)
    return render(request, 'page/news_view.html', {'news':news})
############## attorney_general ###############



def attorney_general(request):
    attorney_general = AttorneyGeneral.objects.order_by('-start_date')

    paginate_by = 4

    paginator = Paginator(attorney_general, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'attorney_general':page_obj,
        'paginator':paginator,
        'page_obj':page_obj

    }
    return render(request, 'page/attorney_general.html', context)





##################################### ###############################

def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            request.session['django_language'] = language
            activate(language)
    else:
        language = request.session.get('django_language')
        if language:
            activate(language)
    return HttpResponseRedirect(reverse('my_path'))

##########################################################################








def attorney_general_view(request, id):
    attorney_general = AttorneyGeneral.objects.get(id=id)
    context = {
        'attorney_general':attorney_general
    }
    return render(request, 'page/attorney_general_view.html', context)